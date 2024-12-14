# Requirements #
import tkinter as tk
from tkinter import *
import tkinter.font



class AccHome(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#3b3b3b')
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        label1 = tk.Label(self, text="Choose Accessory Type", anchor='w',
                          font=("Calibri", 20), bg='#3b3b3b', fg="white")
        label1.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        # Accessory Buttons
        self.button_sleeves = tk.Button(self, text="Sleeves", font=tkinter.font.Font(family="Calibri", size=18, overstrike=1), command=self.sleeve)
        self.button_sleeves.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.15)

        self.button_boxes = tk.Button(self, text="Deck Boxes", font=tkinter.font.Font(family="Calibri", size=18, overstrike=1), command=self.box)
        self.button_boxes.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.15)

        self.button_playmats = tk.Button(self, text="Playmats", font=tkinter.font.Font(family="Calibri", size=18, overstrike=1), command=self.playmat)
        self.button_playmats.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.15)

        self.button_dice = tk.Button(self, text="Dice", font=tkinter.font.Font(family="Calibri", size=18, overstrike=1), command=self.dice)
        self.button_dice.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.15)

        self.button_books = tk.Button(self, text="Collection Books", font=tkinter.font.Font(family="Calibri", size=18, overstrike=1), command=self.book)
        self.button_books.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.15)

        self.button_comics = tk.Button(self, text="Comics", font=("Calibri", 18), command=self.comic)
        self.button_comics.place(relx=0.6, rely=0.6, relwidth=0.3, relheight=0.15)

        # Navigation Buttons
        self.button_back = tk.Button(self, text="Back", font=("Calibri", 14), command=self.back)
        self.button_back.place(relx=0.85, rely=0.9, relwidth=0.12, relheight=0.1)

    def sleeve(self):
        print("Selected Sleeves")

    def box(self):
        print("Selected Deck Boxes")

    def playmat(self):
        print("Selected Playmats")

    def dice(self):
        print("Selected Dice")

    def book(self):
        print("Selected Collection Books")

    def comic(self):
        print("Selected Comics")
        self.master.show_frame("AccCom") # Open comic editor

    def back(self):
        print("Navigate Back")
        self.master.show_frame("MEHome") # Open mod editor home page
