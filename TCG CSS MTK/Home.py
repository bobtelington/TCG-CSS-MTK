# Requirements #
from tkinter import *
import tkinter.font



# Mod editor home page #
class MEHome(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg='#3b3b3b')
        self.gui()

    def gui(self):
        self.label1 = Label(
            self,
            text="Select mod category",
            anchor='w',
            font=tkinter.font.Font(family="Calibri", size=20),
            cursor="arrow",
            state="normal",
            bg="#3b3b3b", fg="white"
        )
        self.label1.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.1)

        self.button1 = Button(
            self,
            text="Figurines",
            font=tkinter.font.Font(family="Calibri", size=20),
            cursor="arrow",
            state="normal",
            command=self.FigEditor
        )
        self.button1.place(relx=0.05, rely=0.15, relwidth=0.4, relheight=0.15)

        self.button2 = Button(
            self,
            text="Accessories",
            font=tkinter.font.Font(family="Calibri", size=20),
            cursor="arrow",
            state="normal",
            command=self.AccEditor
        )
        self.button2.place(relx=0.55, rely=0.15, relwidth=0.4, relheight=0.15)

        self.button3 = Button(
            self,
            text="Tabletop Games",
            font=tkinter.font.Font(family="Calibri", size=20, overstrike=1),
            cursor="arrow",
            state="normal",
            command=self.TTGEditor
        )
        self.button3.place(relx=0.05, rely=0.35, relwidth=0.4, relheight=0.15)

        self.button4 = Button(
            self,
            text="Cards",
            font=tkinter.font.Font(family="Calibri", size=20, overstrike=1),
            cursor="arrow",
            state="normal",
            command=self.CardEditor
        )
        self.button4.place(relx=0.55, rely=0.35, relwidth=0.4, relheight=0.15)

    def FigEditor(self):
        print('FigEditor')
        self.master.show_frame("Fig1") # Open figurine editor

    def AccEditor(self):
        print('AccEditor')
        self.master.show_frame("AccHome") # Open accessory editor

    def TTGEditor(self):
        print('TTGEditor')

    def CardEditor(self):
        print('CardEditor')