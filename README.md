TCG CSS MTK

Overview

TCG CSS MTK is a modding toolkit for TCG Card Shop Simulator. Currently, the only tool is the Mod Editor, but more tools will be added in the future.

Current Features

Basic UI: Though visually simplistic, the program provides navigation for:

Selecting and managing figurines, plushies, and comic book mods.

Editing mod meshes, textures, icons, and names.

Basic database queries for matching items.

Copies original mod files: All edits and changes are made to the copies, leaving the original mod files unaltered.

File Organization: Automatically organizes the new mod files into structured folders for easier management.

Database Integration:

Connects to an SQLite database (e.g., demo.db in the Database/ folder).

Fetches item attributes (e.g., texture, icon, name).

Auto-scaling (Experimental): Optionally scales .obj files based on reference models (requires game files).

Requirements

Python 3.x

Required dependencies (install via pip install -r requirements.txt):

tkinter

Pillow

sqlite3

Installation

For the compiled "just download and run" version:
Insert Nexus Link

Clone the repository:

git clone https://github.com/your-username/TCG-CSS-MTK.git

Navigate to the project directory:

cd TCG-CSS-MTK

Install dependencies:

pip install -r requirements.txt

Usage

Ensure your mod files and database (demo.db) are placed in the appropriate subfolders:

Database/ for the SQLite database.

Game Exports/ for reference models or textures.

Output/ for processed files.

Run the program:

python Main.py

Follow the on-screen instructions to:

Select mod files.

Preview and modify meshes, textures, icons, and names.

Apply experimental auto-scaling to .obj files (requires game files).

Known Limitations

The user interface (UI) is functional but lacks polish.

Code efficiency and optimization are works in progress.

Limited feature set (more features and tools coming soon!)
