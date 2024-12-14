# Requirements #
import os
import subprocess
import VarConfig
import tkinter as tk
from tkinter import filedialog, Frame, Label, Button, Text, Tk, font, ttk
from tkinter.ttk import Combobox
from ComScript import main as run_com_script  # Import ComScript's main function



class AccCom(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#3b3b3b')
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        label1 = tk.Label(self, text="Select Mod Files", anchor='w',
                          font=("Calibri", 20), bg='#3b3b3b', fg="white")
        label1.place(relx=0, rely=0.15, relwidth=1, relheight=0.1)

        # Volume selection
        self.combo1 = ttk.Combobox(
            self,
            font=("Calibri", 16),
            state="readonly",  # Using "readonly" to match typical combobox behavior
        )
        self.combo1['values'] = [f"Vol. {i}" for i in range(1, 13)]
        self.combo1.set("Vol. 1")  # Set default value
        self.combo1.place(relx=0.25, rely=0.02, relwidth=0.2, relheight=0.08)


        # Mod Folder Selection
        button1 = tk.Button(self, text="Mod Folder:", font=("Calibri", 14), command=self.folder)
        button1.place(relx=0.02, rely=0.3, relwidth=0.2, relheight=0.1)

        self.text1 = tk.Text(self, font=("Calibri", 12))
        self.text1.place(relx=0.25, rely=0.3, relwidth=0.7, relheight=0.1)

        # Texture Selection
        button2 = tk.Button(self, text="Texture:", font=("Calibri", 14), command=self.texture)
        button2.place(relx=0.02, rely=0.45, relwidth=0.2, relheight=0.1)

        self.text2 = tk.Text(self, font=("Calibri", 12))
        self.text2.place(relx=0.25, rely=0.45, relwidth=0.7, relheight=0.1)

        # Icon Selection
        button3 = tk.Button(self, text="Icon:", font=("Calibri", 14), command=self.icon)
        button3.place(relx=0.02, rely=0.6, relwidth=0.2, relheight=0.1)

        self.text3 = tk.Text(self, font=("Calibri", 12))
        self.text3.place(relx=0.25, rely=0.6, relwidth=0.7, relheight=0.1)

        # Name Selection
        button4 = tk.Button(self, text="Name:", font=("Calibri", 14), command=self.name)
        button4.place(relx=0.02, rely=0.75, relwidth=0.2, relheight=0.1)

        self.text4 = tk.Text(self, font=("Calibri", 12))
        self.text4.place(relx=0.25, rely=0.75, relwidth=0.7, relheight=0.1)

        # Navigation Buttons
        button_back = tk.Button(self, text="Back", font=("Calibri", 14), command=self.back)
        button_back.place(relx=0.7, rely=0.9, relwidth=0.12, relheight=0.1)

        button_next = tk.Button(self, text="Finish", font=("Calibri", 14), command=self.finish)
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
        auto_name = None
        auto_texture = None
        auto_icon = None

        # Iterate over files in the selected folder
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)

                # Check file types
                if file.endswith(".txt") and not auto_name:
                    auto_name = file_path
                elif file.endswith(".png"):
                    if "icon" in file.lower() and not auto_icon:
                        auto_icon = file_path
                    elif "icon" not in file.lower() and not auto_texture:
                        auto_texture = file_path

                # Stop searching if all files are found
                if auto_name and auto_texture and auto_icon:
                    break

        # Print file paths in the respective text boxes
        self.text2.delete('1.0', 'end')
        self.text2.insert('1.0', auto_texture if auto_texture else "No .png file found")

        self.text3.delete('1.0', 'end')
        self.text3.insert('1.0', auto_icon if auto_icon else "No .png file found")

        self.text4.delete('1.0', 'end')
        self.text4.insert('1.0', auto_name if auto_name else "No .txt file found")

    # Manual file selection #
    def texture(self):
        file = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])
        if file:
            self.text2.delete("1.0", "end")
            self.text2.insert("1.0", file)

    def icon(self):
        file = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])
        if file:
            self.text3.delete("1.0", "end")
            self.text3.insert("1.0", file)

    def name(self):
        file = filedialog.askopenfilename(filetypes=[("TXT Files", "*.txt")])
        if file:
            self.text4.delete("1.0", "end")
            self.text4.insert("1.0", file)

    def back(self):
        print("Navigate Back")
        self.master.show_frame("AccHome") # Open accessory editor

    def finish(self):
        print("Finish")

        # Change global variable values #
        VarConfig.game_target = self.combo1.get().strip()
        print(f"VarConfig.game_target: {VarConfig.game_target}")

        VarConfig.mod_texture = self.text2.get('1.0', 'end').strip()
        print(f"VarConfig.mod_texture: {VarConfig.mod_texture}")

        VarConfig.mod_icon = self.text3.get('1.0', 'end').strip()
        print(f"VarConfig.mod_icon: {VarConfig.mod_icon}")

        VarConfig.mod_name = self.text4.get('1.0', 'end').strip()
        print(f"VarConfig.mod_name: {VarConfig.mod_name}")
        
        # Log for debugging
        print("Debug:")
        print(f"Game target selected: {VarConfig.game_target}")
        print(f"Texture: {VarConfig.mod_texture}")
        print(f"Icon: {VarConfig.mod_icon}")
        print(f"Name: {VarConfig.mod_name}")

        # Call the ComScript functionality directly
        try:
            run_com_script()  # This will execute ComScript's main function
            print("ComScript.py executed successfully.")
        except Exception as e:
            print(f"Error running ComScript: {e}")