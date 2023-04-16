from tkinter import *
from PIL import Image, ImageTk


class TripleImageRow:
    def __init__(self, master=None, images=[], rely=0, size=100):
        self.images = []
        self.image_items = []
        for i in range(len(images)):
            if i >= 3:
                break
            image = Image.open(images[i])
            image = image.resize((size, size), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            label = Label(master, image=image)
            label.place(x=(size * 1.1) * i, rely=rely)
            self.images.append(image)
            self.image_items.append(label)

