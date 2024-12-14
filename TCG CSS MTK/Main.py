# Requirements #
import tkinter as Tk
from Home import MEHome
from Figurines import Fig1, Fig2
from Accessories import AccHome
from Comics import AccCom



# Framework for main window and UI #
class MainWindow(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mod Editor")
        self.geometry("900x600")
        self.minsize(600, 400)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.create_frames()

    def create_frames(self):
        for F in (MEHome, Fig1, Fig2, AccHome, AccCom):
            frame = F(self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MEHome")  # Load initial frame/page

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
