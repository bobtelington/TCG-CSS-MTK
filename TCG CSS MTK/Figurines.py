# Requirements #
import os
import sqlite3
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog, ttk, BooleanVar
from PIL import Image, ImageTk
import VarConfig
import tkinter.font
from FigScript import main as run_fig_script  # Import FigScript's main function



# Page 1: File selection #
class Fig1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#3b3b3b')
        self.create_widgets()

    def create_widgets(self):
        # Label
        label1 = tk.Label(self, text="Select Mod Files", anchor='w', font=("Calibri", 20), bg='#3b3b3b', fg="white")
        label1.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        # Mod Folder Selection
        button1 = tk.Button(self, text="Mod Folder:", font=("Calibri", 14), command=self.folder)
        button1.place(relx=0.02, rely=0.15, relwidth=0.2, relheight=0.1)

        self.text1 = tk.Text(self, font=("Calibri", 12))
        self.text1.place(relx=0.25, rely=0.15, relwidth=0.7, relheight=0.1)

        # Mesh Selection
        button2 = tk.Button(self, text="Mesh:", font=("Calibri", 14), command=self.mesh)
        button2.place(relx=0.02, rely=0.3, relwidth=0.2, relheight=0.1)

        self.text2 = tk.Text(self, font=("Calibri", 12))
        self.text2.place(relx=0.25, rely=0.3, relwidth=0.7, relheight=0.1)

        # Texture Selection
        button3 = tk.Button(self, text="Texture:", font=("Calibri", 14), command=self.texture)
        button3.place(relx=0.02, rely=0.45, relwidth=0.2, relheight=0.1)

        self.text3 = tk.Text(self, font=("Calibri", 12))
        self.text3.place(relx=0.25, rely=0.45, relwidth=0.7, relheight=0.1)

        # Icon Selection
        button4 = tk.Button(self, text="Icon:", font=("Calibri", 14), command=self.icon)
        button4.place(relx=0.02, rely=0.6, relwidth=0.2, relheight=0.1)

        self.text4 = tk.Text(self, font=("Calibri", 12))
        self.text4.place(relx=0.25, rely=0.6, relwidth=0.7, relheight=0.1)

        # Name Selection
        button5 = tk.Button(self, text="Name:", font=("Calibri", 14), command=self.name)
        button5.place(relx=0.02, rely=0.75, relwidth=0.2, relheight=0.1)

        self.text5 = tk.Text(self, font=("Calibri", 12))
        self.text5.place(relx=0.25, rely=0.75, relwidth=0.7, relheight=0.1)

        # Navigation Buttons
        button_back = tk.Button(self, text="Back", font=("Calibri", 14), command=self.back)
        button_back.place(relx=0.7, rely=0.9, relwidth=0.12, relheight=0.1)

        button_next = tk.Button(self, text="Next", font=("Calibri", 14), command=self.next)
        button_next.place(relx=0.85, rely=0.9, relwidth=0.12, relheight=0.1)

    def folder(self):
        print('Folder')
        folder = filedialog.askdirectory(title="Select Mod Folder")
        if folder:
            folder = os.path.normpath(folder)
            self.text1.delete('1.0', 'end')  # Clear existing text
            self.text1.insert('1.0', folder)  # Insert the selected folder path

        # Auto find mod files #
        # Initialize file variables
        auto_mesh = None
        auto_name = None
        auto_texture = None
        auto_icon = None

        # Iterate over files in the selected folder
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)

                # Check file types
                if file.endswith(".obj") and not auto_mesh:
                    auto_mesh = file_path
                elif file.endswith(".txt") and not auto_name:
                    auto_name = file_path
                elif file.endswith(".png"):
                    if "icon" in file.lower() and not auto_icon:
                        auto_icon = file_path
                    elif "icon" not in file.lower() and not auto_texture:
                        auto_texture = file_path

                # Stop searching if all files are found
                if auto_mesh and auto_name and auto_texture and auto_icon:
                    break

        # Print file paths in the respective text boxes
        self.text2.delete('1.0', 'end')
        self.text2.insert('1.0', auto_mesh if auto_mesh else "No .obj file found")

        self.text3.delete('1.0', 'end')
        self.text3.insert('1.0', auto_texture if auto_texture else "No .png file found")

        self.text4.delete('1.0', 'end')
        self.text4.insert('1.0', auto_icon if auto_icon else "No .png file found")

        self.text5.delete('1.0', 'end')
        self.text5.insert('1.0', auto_name if auto_name else "No .txt file found")

    # Manual file selection #
    def mesh(self):
        file = filedialog.askopenfilename(filetypes=[("OBJ Files", "*.obj")])
        if file:
            self.text2.delete("1.0", "end")
            self.text2.insert("1.0", file)

    def texture(self):
        file = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])
        if file:
            self.text3.delete("1.0", "end")
            self.text3.insert("1.0", file)

    def icon(self):
        file = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])
        if file:
            self.text4.delete("1.0", "end")
            self.text4.insert("1.0", file)

    def name(self):
        file = filedialog.askopenfilename(filetypes=[("TXT Files", "*.txt")])
        if file:
            self.text5.delete("1.0", "end")
            self.text5.insert("1.0", file)

    def back(self):
        print("Back")
        self.master.show_frame("MEHome")  # Open mod editor home page

    def next(self):
        print("Next")

        # Change global variable values #
        VarConfig.mod_mesh = self.text2.get('1.0', 'end').strip()
        print(f"VarConfig.mod_mesh: {VarConfig.mod_mesh}")

        VarConfig.mod_texture = self.text3.get('1.0', 'end').strip()
        print(f"VarConfig.mod_texture: {VarConfig.mod_texture}")

        VarConfig.mod_icon = self.text4.get('1.0', 'end').strip()
        print(f"VarConfig.mod_icon: {VarConfig.mod_icon}")

        VarConfig.mod_name = self.text5.get('1.0', 'end').strip()
        print(f"VarConfig.mod_name: {VarConfig.mod_name}")

        self.master.show_frame("Fig2")  # Open figurine page 2


class Fig2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#3b3b3b')
        # Check for Mesh and Texture2D folders
        self.mesh_folder_exists = os.path.exists(os.path.join(os.getcwd(), "Game Exports", "Mesh"))
        self.texture2d_folder_exists = os.path.exists(os.path.join(os.getcwd(), "Game Exports", "Texture2D"))

        self.auto_scale_var = tk.BooleanVar(value=False)  # Local BooleanVar
        self.image_tk = None  # Store the current image
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        self.label1 = tk.Label(self, text="Select Game Item", anchor='w', font=("Calibri", 20), bg='#3b3b3b', fg="white")
        self.label1.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        # Category Combobox
        self.combo1 = ttk.Combobox(self, font=("Calibri", 16), state="readonly")
        self.combo1['values'] = ("Plushies", "Figurines")
        self.combo1.set("Category")
        self.combo1.bind("<<ComboboxSelected>>", self.update_combo2)
        self.combo1.place(relx=0.1, rely=0.2, relwidth=0.4, relheight=0.08)

        # Item Combobox
        self.combo2 = ttk.Combobox(self, font=("Calibri", 16), state="readonly")
        self.combo2['values'] = ("Item",)
        self.combo2.set("Item")
        self.combo2.bind("<<ComboboxSelected>>", self.on_combo2_select)
        self.combo2.place(relx=0.1, rely=0.35, relwidth=0.4, relheight=0.08)

        # Auto scale option
        auto_scale_text = "Auto Scale"
        if not self.mesh_folder_exists:
            auto_scale_text = "\u0336".join(auto_scale_text)  # Add strikeout effect

        self.check1 = tk.Checkbutton(
            self,
            text=auto_scale_text,
            anchor='w',
            font=("Calibri", 16),
            bg='#3b3b3b',
            fg="white",
            variable=self.auto_scale_var,
            command=self.toggle_auto_scale
        )
        self.check1.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.08)

        # Disable the checkbox if Mesh folder is missing
        if not self.mesh_folder_exists:
            self.check1.config(state="disabled")

        # Image Display Canvas
        self.image1 = tk.Canvas(self, bg='white')
        self.image1.place(relx=0.55, rely=0.2, relwidth=0.35, relheight=0.35)

        # If Texture2D folder is missing, display the placeholder message
        if not self.texture2d_folder_exists:
            self.display_placeholder_text("Provide game files for previews")

        # Navigation Buttons
        self.button_back = tk.Button(self, text="Back", font=("Calibri", 14), command=self.back)
        self.button_back.place(relx=0.7, rely=0.9, relwidth=0.12, relheight=0.08)

        self.button_finish = tk.Button(self, text="Finish", font=("Calibri", 14), command=self.finish)
        self.button_finish.place(relx=0.85, rely=0.9, relwidth=0.12, relheight=0.08)

    def toggle_auto_scale(self):
        if not self.mesh_folder_exists:
            # Show a popup message
            messagebox.showerror("Error", "Provide game files for auto scale")
        else:
            VarConfig.auto_scale = self.auto_scale_var.get()
            print(f"Auto scale is set to: {VarConfig.auto_scale}")

    def display_placeholder_text(self, text):
        # Display a placeholder message on the canvas
        self.image1.delete("all")
        self.image1.create_text(
            self.image1.winfo_width() // 2,
            self.image1.winfo_height() // 2,
            text=text,
            fill="gray",
            font=("Calibri", 16)
        )

    def display_image(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.resize((self.image1.winfo_width(), self.image1.winfo_height()), Image.LANCZOS)
            self.image_tk = ImageTk.PhotoImage(img)

            # Clear canvas and display new image
            self.image1.delete("all")
            self.image1.create_image(0, 0, anchor="nw", image=self.image_tk)
        except Exception as e:
            print(f"Error displaying image: {e}")
            if self.texture2d_folder_exists:
                self.display_placeholder_text("Image Unavailable")
            else:
                self.display_placeholder_text("Provide game files for previews")

    def on_combo2_select(self, event):
        selected_item = self.combo2.get()
        if not selected_item:
            self.display_unavailable()
            return

        icon_filename = self.fetch_icon_from_db(selected_item)
        if not icon_filename:
            self.display_unavailable()
            return

        texture2d_path = os.path.join(os.getcwd(), "Game Exports", "Texture2D")
        icon_path = os.path.join(texture2d_path, icon_filename)

        if os.path.exists(icon_path):
            self.display_image(icon_path)
        else:
            self.display_unavailable()

    def display_unavailable(self):
        if self.texture2d_folder_exists:
            self.display_placeholder_text("Image Unavailable")
        else:
            self.display_placeholder_text("Provide game files for previews")

    def update_combo2(self, event):
        selected_category = self.combo1.get()
        if selected_category == "Plushies":
            self.combo2['values'] = ("Pigni", "Nanomite", "Ministar", "Nocti", "Blazoar", "Kingstar", "Bonfiox", "ToonZ")
        elif selected_category == "Figurines":
            self.combo2['values'] = ("Burpig", "Decimite", "Trickstar", "Lunight", "Inferhog", "Meganite", "Princestar",
                                     "Vampicant", "Giganite", "Dracunix", "Drilceros")
        else:
            self.combo2['values'] = ()
        self.combo2.set("Item")  # Reset placeholder text for combo2

    def fetch_icon_from_db(self, item_name):
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
            icon_column = columns[5][1]  # Icon is the 5th column

            # Now query the table for the matching Item
            cursor.execute(f"SELECT {icon_column} FROM {table_name} WHERE {item_column} = ?", (item_name,))
            result = cursor.fetchone()
            conn.close()

            if result:
                return result[0]  # The icon filename
            else:
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None        

    def back(self):
        print("Navigate Back")
        self.master.show_frame("Fig1")  # Open figurine page 1

    def finish(self):
        # Update global variables
        VarConfig.game_target = self.combo2.get()

        # Log for debugging
        print("Debug:")
        print(f"Game target selected: {VarConfig.game_target}")
        print(f"Mesh: {VarConfig.mod_mesh}")
        print(f"Texture: {VarConfig.mod_texture}")
        print(f"Icon: {VarConfig.mod_icon}")
        print(f"Name: {VarConfig.mod_name}")
        print(f"Auto scale: {VarConfig.auto_scale}")

        # Call the FigScript functionality directly
        try:
            run_fig_script()  # This will execute FigScript's main function
            print("FigScript.py executed successfully.")
        except Exception as e:
            print(f"Error running FigScript: {e}")