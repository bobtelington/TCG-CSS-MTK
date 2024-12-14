import sys
import os
import shutil
import sqlite3
import VarConfig

def main():
    # Print the values
    print("Script Output:")
    print("Game target: {}".format(VarConfig.game_target))
    print("Mesh: {}".format(VarConfig.mod_mesh))
    print("Texture: {}".format(VarConfig.mod_texture))
    print("Icon: {}".format(VarConfig.mod_icon))
    print("Name: {}".format(VarConfig.mod_name))
    print("Scale: {}".format(VarConfig.auto_scale))


    # Locate the destination folder path
    destination_folder = VarConfig.output_folder

    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Create output folder structure
    objects_meshes_dir = os.path.join(destination_folder, 'TextureReplacer', 'objects_meshes')
    if not os.path.exists(objects_meshes_dir):
        os.makedirs(objects_meshes_dir)

    objects_textures_dir = os.path.join(destination_folder, 'TextureReplacer', 'objects_textures')
    if not os.path.exists(objects_textures_dir):
        os.makedirs(objects_textures_dir)

    objects_data_dir = os.path.join(destination_folder, 'TextureReplacer', 'objects_data', 'figurines')
    if not os.path.exists(objects_data_dir):
        os.makedirs(objects_data_dir)

    # Copy files to the appropriate directories
    try:
        shutil.copy(VarConfig.mod_mesh, os.path.join(objects_meshes_dir, os.path.basename(VarConfig.mod_mesh)))
        shutil.copy(VarConfig.mod_texture, os.path.join(objects_textures_dir, os.path.basename(VarConfig.mod_texture)))
        shutil.copy(VarConfig.mod_icon, os.path.join(objects_textures_dir, os.path.basename(VarConfig.mod_icon)))
        shutil.copy(VarConfig.mod_name, os.path.join(objects_data_dir, os.path.basename(VarConfig.mod_name)))
        
        print("Game target: {}".format(VarConfig.game_target))
        print("Files copied successfully.")
    except Exception as e:
        print(f"Error copying files: {e}")
        return





    def get_obj_vertices(file_path):
        """Extract vertices from an .obj file."""
        vertices = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if line.startswith('v '):  # Only process lines starting with 'v ' (vertices)
                        parts = line.split()
                        x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                        vertices.append((x, y, z))
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        return vertices

    def apply_scaling(vertices, scale_factor):
        """Apply a scale factor to a list of vertices."""
        scaled_vertices = [(x * scale_factor, y * scale_factor, z * scale_factor) for x, y, z in vertices]
        return scaled_vertices

    def reposition_origin(vertices, reference_bottom_y, reference_bottom_x, reference_bottom_z):
        """Reposition the origin of the vertices so that the bottom aligns with the reference model's bottom."""
        current_bottom_y = min(y for x, y, z in vertices)
        current_bottom_x = min(x for x, y, z in vertices)
        current_bottom_z = min(z for x, y, z in vertices)
        
        # Calculate the offset for y, x, and z axes
        offset_y = reference_bottom_y - current_bottom_y
        offset_x = reference_bottom_x - current_bottom_x
        offset_z = reference_bottom_z - current_bottom_z

        # Reposition all vertices
        repositioned_vertices = [(x + offset_x, y + offset_y, z + offset_z) for x, y, z in vertices]
        return repositioned_vertices

    def write_scaled_obj(file_path, original_lines, scaled_vertices):
        """Write the scaled and repositioned vertices back to a new .obj file."""
        try:
            with open(file_path, 'w') as file:
                vertex_index = 0
                for line in original_lines:
                    if line.startswith('v '):  # Replace vertex lines with scaled and repositioned vertices
                        x, y, z = scaled_vertices[vertex_index]
                        file.write(f"v {x} {y} {z}\n")
                        vertex_index += 1
                    else:
                        file.write(line)  # Keep non-vertex lines unchanged
            print(f"Scaled and repositioned .obj file written to {file_path}.")
        except Exception as e:
            print(f"Error writing scaled .obj file: {e}")

    def rescale_and_reposition_obj(output_file_path, game_export_file_path):
        """Rescale the .obj file from Output to match the scale of the one in Game Exports/Mesh, and reposition the origin."""
        output_vertices = get_obj_vertices(output_file_path)
        game_export_vertices = get_obj_vertices(game_export_file_path)
        
        if not output_vertices or not game_export_vertices:
            print("Error: Could not extract vertices from one or both .obj files.")
            return

        # Calculate the bounding box for the output and game export vertices
        def get_bounding_box(vertices):
            min_x = min_y = min_z = float('inf')
            max_x = max_y = max_z = float('-inf')
            for (x, y, z) in vertices:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                min_z = min(min_z, z)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                max_z = max(max_z, z)
            return (min_x, min_y, min_z), (max_x, max_y, max_z)
        
        output_min, output_max = get_bounding_box(output_vertices)
        game_export_min, game_export_max = get_bounding_box(game_export_vertices)

        # Calculate the scale factor based on the bounding boxes
        output_width = output_max[0] - output_min[0]
        output_height = output_max[1] - output_min[1]
        output_depth = output_max[2] - output_min[2]
        
        game_export_width = game_export_max[0] - game_export_min[0]
        game_export_height = game_export_max[1] - game_export_min[1]
        game_export_depth = game_export_max[2] - game_export_min[2]

        # Compute the scaling factors for each dimension
        scale_x = game_export_width / output_width
        scale_y = game_export_height / output_height
        scale_z = game_export_depth / output_depth
        
        # Average scale factor
        scale_factor = (scale_x + scale_y + scale_z) / 3

        print(f"Scaling factor: {scale_factor:.4f}")

        # Apply the scaling to the output vertices
        scaled_vertices = apply_scaling(output_vertices, scale_factor)

        # Get the bottom of the game export model (the min y, x, z values)
        reference_bottom_y = min(y for x, y, z in game_export_vertices)
        reference_bottom_x = min(x for x, y, z in game_export_vertices)
        reference_bottom_z = min(z for x, y, z in game_export_vertices)

        # Reposition the output vertices to match the bottom of the reference model
        repositioned_vertices = reposition_origin(scaled_vertices, reference_bottom_y, reference_bottom_x, reference_bottom_z)

        # Read the original .obj file lines
        with open(output_file_path, 'r') as file:
            original_lines = file.readlines()

        # Write the scaled and repositioned .obj file to the same location
        write_scaled_obj(output_file_path, original_lines, repositioned_vertices)





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

        # The second column is 'Item', the third is 'Mesh', the fourth is 'Texture', the fifth is 'Icon', and the sixth is 'Name'
        item_column = columns[2][1]  # Item is the 2nd column
        mesh_column = columns[3][1]  # Mesh is the 3rd column
        texture_column = columns[4][1]  # Texture is the 4th column
        icon_column = columns[5][1]  # Icon is the 5th column
        name_column = columns[6][1]  # Name is the 6th column

        # Now query the table for the VarConfig.game_target match in the 'Item' column
        cursor.execute(f"SELECT {mesh_column}, {texture_column}, {icon_column}, {name_column} FROM {table_name} WHERE {item_column} = ?", (VarConfig.game_target,))
        result = cursor.fetchone()

        if result:
            # Rename the mesh file
            mesh_filename = result[0]  # The value from the Mesh column
            new_mesh_path = os.path.join(objects_meshes_dir, mesh_filename)
            old_mesh_path = os.path.join(objects_meshes_dir, os.path.basename(VarConfig.mod_mesh))
            os.rename(old_mesh_path, new_mesh_path)
            print(f"Mesh file renamed to: {mesh_filename}")

            # Rename the texture file
            texture_filename = result[1]  # The value from the Texture column
            new_texture_path = os.path.join(objects_textures_dir, texture_filename)
            old_texture_path = os.path.join(objects_textures_dir, os.path.basename(VarConfig.mod_texture))
            os.rename(old_texture_path, new_texture_path)
            print(f"Texture file renamed to: {texture_filename}")

            # Rename the icon file
            icon_filename = result[2]  # The value from the Icon column
            new_icon_path = os.path.join(objects_textures_dir, icon_filename)
            old_icon_path = os.path.join(objects_textures_dir, os.path.basename(VarConfig.mod_icon))
            os.rename(old_icon_path, new_icon_path)
            print(f"Icon file renamed to: {icon_filename}")

            # Rename the name file
            name_filename = result[3]  # The value from the Name column
            new_name_path = os.path.join(objects_data_dir, name_filename)
            old_name_path = os.path.join(objects_data_dir, os.path.basename(VarConfig.mod_name))
            os.rename(old_name_path, new_name_path)
            print(f"Name file renamed to: {name_filename}")

        else:
            print(f"No match found for VarConfig.game_target '{VarConfig.game_target}' in the database.")

        # Close the database connection
        conn.close()

        # If auto_scale is True, find the .obj file in Output and rescale it based on the game export
        if VarConfig.auto_scale:
            output_obj_path = os.path.join(objects_meshes_dir, mesh_filename)
            
            game_export_obj_path = VarConfig.get_game_export_path('Mesh', mesh_filename)
            
            if os.path.exists(output_obj_path) and os.path.exists(game_export_obj_path):
                rescale_and_reposition_obj(output_obj_path, game_export_obj_path)
            else:
                print(f"Error: Could not find both the output and game export .obj files for rescaling.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return


    print("Run script")


if __name__ == "__main__":
    main()