import os
import shutil
import sqlite3
import VarConfig

def main():
    # Print the values
    print("Script Output:")
    print("Game target: {}".format(VarConfig.game_target))
    print("Texture: {}".format(VarConfig.mod_texture))
    print("Icon: {}".format(VarConfig.mod_icon))
    print("Name: {}".format(VarConfig.mod_name))


    # Locate the destination folder path
    destination_folder = VarConfig.output_folder

    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Create output folder structure
    objects_textures_dir = os.path.join(destination_folder, 'TextureReplacer', 'objects_textures')
    if not os.path.exists(objects_textures_dir):
        os.makedirs(objects_textures_dir)

    objects_data_dir = os.path.join(destination_folder, 'TextureReplacer', 'objects_data', 'accessories')
    if not os.path.exists(objects_data_dir):
        os.makedirs(objects_data_dir)

    # Copy files to the appropriate directories
    try:
        shutil.copy(VarConfig.mod_texture, os.path.join(objects_textures_dir, os.path.basename(VarConfig.mod_texture)))
        shutil.copy(VarConfig.mod_icon, os.path.join(objects_textures_dir, os.path.basename(VarConfig.mod_icon)))
        shutil.copy(VarConfig.mod_name, os.path.join(objects_data_dir, os.path.basename(VarConfig.mod_name)))
        
        print("Game target: {}".format(VarConfig.game_target))
        print("Files copied successfully.")
    except Exception as e:
        print(f"Error copying files: {e}")
        return



    # Connect to the SQLite database (demo.db in the Database folder)
    db_path = VarConfig.get_database_path('demo.db')
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Retrieve the name of the first table in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if len(tables) == 0:
            print("No tables found in the database.")
            return

        # Fetch column names from the first table
        table_name = tables[0][0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        if not columns:
            print("No columns found in the table.")
            return

        # The second column is 'Item', the fourth is 'Texture', the fifth is 'Icon', and the sixth is 'Name'
        item_column = columns[2][1]  # Item is the 2nd column
        texture_column = columns[4][1]  # Texture is the 4th column
        icon_column = columns[5][1]  # Icon is the 5th column
        name_column = columns[6][1]  # Name is the 6th column

        # Now query the table for the VarConfig.game_target match in the 'Item' column
        cursor.execute(f"SELECT {texture_column}, {icon_column}, {name_column} FROM {table_name} WHERE {item_column} = ?", (VarConfig.game_target,))
        result = cursor.fetchone()

        if result:
            # Rename the texture file
            texture_filename = result[0]  # The value from the Texture column
            new_texture_path = os.path.join(objects_textures_dir, texture_filename)
            old_texture_path = os.path.join(objects_textures_dir, os.path.basename(VarConfig.mod_texture))
            os.rename(old_texture_path, new_texture_path)
            print(f"Texture file renamed to: {texture_filename}")

            # Rename the icon file
            icon_filename = result[1]  # The value from the Icon column
            new_icon_path = os.path.join(objects_textures_dir, icon_filename)
            old_icon_path = os.path.join(objects_textures_dir, os.path.basename(VarConfig.mod_icon))
            os.rename(old_icon_path, new_icon_path)
            print(f"Icon file renamed to: {icon_filename}")

            # Rename the name file
            name_filename = result[2]  # The value from the Name column
            new_name_path = os.path.join(objects_data_dir, name_filename)
            old_name_path = os.path.join(objects_data_dir, os.path.basename(VarConfig.mod_name))
            os.rename(old_name_path, new_name_path)
            print(f"Name file renamed to: {name_filename}")

        else:
            print(f"No match found for VarConfig.game_target '{VarConfig.game_target}' in the database.")

        # Close the database connection
        conn.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return


    print("Script finished running")


if __name__ == "__main__":
    main()