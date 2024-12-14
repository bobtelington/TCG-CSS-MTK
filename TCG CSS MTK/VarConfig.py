# Requirements #
import os
import sys



# Locate and save root directory and subfolders #
# Root directory
if getattr(sys, 'frozen', False):  # If running as a compiled executable
    root_directory = os.path.dirname(sys.executable)
else:  # If running as a script
    root_directory = os.path.dirname(os.path.abspath(__file__))

# Subfolders
database_folder = os.path.join(root_directory, "Database")
game_exports_folder = os.path.join(root_directory, "Game Exports")
output_folder = os.path.join(root_directory, "Output")



# Global Variables #
mod_folder = None
mod_mesh = None
mod_texture = None
mod_icon = None
mod_name = None
game_target = None
auto_scale = False
auto_scale_base = False
auto_flip = False



# Utility functions #
def get_database_path(filename):
    """Get the full path to a database file in the Database folder."""
    return os.path.join(database_folder, filename)

def get_game_export_path(subfolder, filename):
    """Get the full path to a file in the Game Exports subfolder."""
    return os.path.join(game_exports_folder, subfolder, filename)

def get_output_path(subfolder, filename):
    """Get the full path to a file in the Output folder."""
    return os.path.join(output_folder, subfolder, filename)