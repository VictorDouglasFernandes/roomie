from tkinter import *
from PIL import Image, ImageTk


class ImageClickable:
    def __init__(self, master=None, image_path=None, size=100, rely=0, on_tap=None):
        if image_path is not None:
            self.image = Image.open(image_path)
            self.image = self.image.resize((size, size), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.image)
            self.label = Label(master, image=self.image)
            self.label.place(relx=0, rely=rely)
            if on_tap is not None:
                self.label.bind("<Button-1>", lambda e: on_tap(image_path))

    def hide(self):
        if self.image is not None:
            self.label.place_forget()