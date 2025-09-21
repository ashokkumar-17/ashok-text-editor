# src/editor.py

"""
Editor Module for Text Editor
=============================

Provides the Editor class which manages the Tkinter GUI,
menus, text area, status bar, and actions.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from .file_ops import open_file, save_file
from .utils import show_status_message, show_info, ask_find_text


class Editor:
    def __init__(self, root=None):
        # Initialize main window
        self.root = root or tk.Tk()
        self.root.title("Untitled - Ashok's text editor")
        self.root.geometry("800x600")

        # Track current file path
        self.file_path = None

        # Create main text widget
        self.text = tk.Text(self.root, undo=True, wrap="word")
        self.text.pack(fill="both", expand=True)

        # Create a status bar
        self.status_var = tk.StringVar()
        self.status_bar = tk.Label(self.root, textvariable=self.status_var, anchor="w")
        self.status_bar.pack(side="bottom", fill="x")

        # Create menu bar
        self.create_menus()

        # Bind keyboard shortcuts
        self.bind_shortcuts()

    # ----------------- Menu Setup -----------------
    def create_menus(self):
        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open...", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.undo)
        edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: self.text.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: self.text.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: self.text.event_generate("<<Paste>>"))
        edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=lambda: self.text.tag_add("sel", "1.0", "end"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", accelerator="Ctrl+F", command=self.find_text)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    # ----------------- File Actions -----------------
    def new_file(self):
        if self.confirm_discard_changes():
            self.text.delete("1.0", tk.END)
            self.file_path = None
            self.root.title("Untitled - Ashok's text editor")
            show_status_message(self.status_var, "New file created")

    def open_file(self):
        if self.confirm_discard_changes():
            content, path = open_file(self.root)
            if content is not None:
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", content)
                self.file_path = path
                self.root.title(f"{self.file_path} - Ashok's text editor")
                show_status_message(self.status_var, f"Opened: {self.file_path}")

    def save_file(self):
        content = self.text.get("1.0", tk.END)
        path = save_file(self.root, content, self.file_path)
        if path:
            self.file_path = path
            self.root.title(f"{self.file_path} - Ashok's text editor")
            show_status_message(self.status_var, f"Saved: {self.file_path}")

    def save_as_file(self):
        content = self.text.get("1.0", tk.END)
        path = save_file(self.root, content, None)
        if path:
            self.file_path = path
            self.root.title(f"{self.file_path} - Ashok's text editor")
            show_status_message(self.status_var, f"Saved as: {self.file_path}")

    def exit_editor(self):
        if self.confirm_discard_changes():
            self.root.destroy()

    def confirm_discard_changes(self):
        """
        Confirm with the user if unsaved changes exist.
        Returns True if safe to continue, False to cancel action.
        """
        if self.text.edit_modified():
            result = messagebox.askyesnocancel("Unsaved Changes", "Do you want to save changes?")
            if result:  # Yes
                self.save_file()
                return True
            elif result is False:  # No
                return True
            else:  # Cancel
                return False
        return True

    # ----------------- Edit Actions -----------------
    def undo(self):
        try:
            self.text.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.text.edit_redo()
        except tk.TclError:
            pass

    def find_text(self):
        query = ask_find_text(self.root)
        if query:
            start = "1.0"
            self.text.tag_remove("highlight", "1.0", tk.END)
            while True:
                start = self.text.search(query, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(query)}c"
                self.text.tag_add("highlight", start, end)
                start = end
            self.text.tag_config("highlight", background="yellow", foreground="black")
            show_status_message(self.status_var, f"Found: {query}")

    # ----------------- Help -----------------
    def show_about(self):
        show_info("About", "Ashok's text editor\nBuilt with Python and Tkinter", self.root)

    # ----------------- Shortcuts -----------------
    def bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-S>", lambda e: self.save_as_file())
        self.root.bind("<Control-z>", lambda e: self.undo())
        self.root.bind("<Control-y>", lambda e: self.redo())
        self.root.bind("<Control-f>", lambda e: self.find_text())
        self.root.bind("<Control-a>", lambda e: self.text.tag_add("sel", "1.0", "end"))

    # ----------------- Run -----------------
    def run(self):
        self.root.mainloop()
