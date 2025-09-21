# src/file_ops.py

"""
File Operations Module
======================

Handles opening and saving text files with Tkinter dialogs.
"""

import tkinter as tk
from tkinter import filedialog
from typing import Optional, Tuple


def open_file(parent) -> Tuple[Optional[str], Optional[str]]:
    """
    Open a file dialog and read its content.

    Args:
        parent: Tkinter root or Toplevel for dialog parenting

    Returns:
        tuple: (content, path)
            - content: str file content, or None if cancelled
            - path: str file path, or None if cancelled
    """
    path = filedialog.askopenfilename(
        parent=parent,
        title="Open File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not path:
        return None, None

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return content, path
    except Exception as e:
        tk.messagebox.showerror("Error", f"Could not open file:\n{e}", parent=parent)
        return None, None


def save_file(parent, content: str, file_path: Optional[str]) -> Optional[str]:
    """
    Save text content to a file. If file_path is None, show Save As dialog.

    Args:
        parent: Tkinter root or Toplevel
        content: str, text to save
        file_path: str or None

    Returns:
        str: path where file was saved, or None if cancelled/error
    """
    if not file_path:
        file_path = filedialog.asksaveasfilename(
            parent=parent,
            title="Save File As",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not file_path:
            return None

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path
    except Exception as e:
        tk.messagebox.showerror("Error", f"Could not save file:\n{e}", parent=parent)
        return None
