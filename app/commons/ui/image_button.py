import os
import cv2
from tkinter import *
from fileinput import filename
from tkinter import filedialog
from app.commons.image.path import Path

from app.commons.colors.colors import *
from app.commons.fonts.fonts import jasmineUPC8


class ImageButton:
    def __init__(self, master=None, text="- - -", rely=0.9, validation=None, on_add=None):
        self.validation = validation
        self.on_add = on_add

        self.label = Label(master, text=text, font=jasmineUPC8, bg=kWhite, fg=kYellow)
        self.label.place(relx=0, rely=rely, relheight=0.1, relwidth=0.4)

        self.button = Button(master, text="ENVIAR\nIMAGENS", bg=kYellow, fg=kWhite, command=self.load_image)
        self.button.place(relx=0.6, rely=rely, relheight=0.1, relwidth=0.4)

    def load_image(self):
        if self.validation != None:
            if not self.validation():
                return
        self.filename = filedialog.askopenfilename()
        if self.filename:
            image = cv2.imread(self.filename)
            # Ajustar nome
            self.filepath = os.path.join(Path.IMAGE.value, os.path.basename("name." + self.filename.split(".")[1]))
            cv2.imwrite(self.filepath, image)
            print(self.filepath)
            if self.on_add != None:
                self.on_add(self.filepath)
