 # Text Editor

A simple Word Processor / Text Editor built with **Python and Tkinter**, similar to Notepad or Notepad++.  

It allows users to create, open, edit, and save plain-text files, with menus for common actions and keyboard shortcuts.

---

## Features

### File Menu
- **New** – Create a new document
- **Open** – Open an existing text file
- **Save** – Save current file
- **Save As** – Save to a new file
- **Exit** – Exit the editor (prompts to save unsaved changes)

### Edit Menu
- **Undo / Redo** – Undo or redo changes
- **Cut / Copy / Paste** – Standard clipboard operations
- **Select All** – Select all text
- **Find** – Search for text in the document

### Help Menu
- **About** – Displays application information

### Other Features
- Large editable text area with **undo/redo support**
- Status bar for notifications
- Keyboard shortcuts:
  - `Ctrl+N` → New file
  - `Ctrl+O` → Open file
  - `Ctrl+S` → Save file
  - `Ctrl+Shift+S` → Save As
  - `Ctrl+Z` → Undo
  - `Ctrl+Y` → Redo
  - `Ctrl+F` → Find
  - `Ctrl+A` → Select All

---

## Directory Structure

text_editor/
│
├── src/ # Source code
│ ├── init.py
│ ├── main.py # Launches the app
│ ├── editor.py # Editor GUI and actions
│ ├── file_ops.py # File handling
│ └── utils.py # Helper functions
│
├── assets/ # Icons and images
│ ├── icon.png
│ └── splash.png
│
├── tests/ # Unit tests
│ └── test_file_ops.py
│
├── requirements.txt # Python dependencies
├── README.md
└── LICENSE

---

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd text_editor

2.(Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows


3.Install dependencies:
pip install -r requirements.txt

Running the Editor

From the src folder:
python -m src.main


Or if running from the project root:
python -m src.main

Testing
Run unit tests for file operations:
python -m unittest discover -s tests


Or, if using pytest:
pytest tests
Future Enhancements
Tabs for multiple files
Syntax highlighting for programming languages
Custom themes and fonts
Autosave functionality
Splash screen at startup
Plugin system

how to run: cd C:\Users\ashok\OneDrive\Desktop\text_editor
python -m src.main