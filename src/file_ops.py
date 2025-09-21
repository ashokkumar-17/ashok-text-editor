 # src/file_ops.py

"""
File Operations Module for Text Editor
======================================

Provides functions for opening, saving, and saving as text files using Tkinter dialogs.
"""

import tkinter as tk
from tkinter import filedialog, messagebox

def open_file(parent):
    """
    Open a text file and return its content and path.
    
    Args:
        parent: Tkinter root or Toplevel (used as parent for dialogs)
    
    Returns:
        tuple: (file_content:str, file_path:str) or (None, None) if cancelled
    """
    file_path = filedialog.askopenfilename(
        parent=parent,
        title="Open File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return None, None

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content, file_path
    except Exception as e:
        messagebox.showerror("Open File Error", f"Could not open file:\n{e}", parent=parent)
        return None, None

def save_file(parent, content, file_path=None):
    """
    Save content to a file. If file_path is None, prompt Save As dialog.
    
    Args:
        parent: Tkinter root or Toplevel
        content: str, text to save
        file_path: optional str, existing file path
    
    Returns:
        str: file path saved to, or None if cancelled/error
    """
    if not file_path:
        file_path = filedialog.asksaveasfilename(
            parent=parent,
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save As"
        )
        if not file_path:
            return None

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path
    except Exception as e:
        messagebox.showerror("Save File Error", f"Could not save file:\n{e}", parent=parent)
        return None
