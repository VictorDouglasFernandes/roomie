from tkinter import *
from fileinput import filename
from tkinter import filedialog

from app.commons.colors.colors import *
from app.commons.fonts.fonts import jasmineUPC8


class ImageButton:
    def __init__(self, master=None, text="- - -", rely=0.85):
        self.label = Label(master, text=text, font=jasmineUPC8, bg=kWhite, fg=kYellow)
        self.label.place(relx=0, rely=rely, relheight=0.15, relwidth=0.4)

        self.button = Button(master, text="ENVIAR\nIMAGENS", bg=kYellow, fg=kWhite, command=self.load_image)
        self.button.place(relx=0.6, rely=rely, relheight=0.15, relwidth=0.4)

    def load_image(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            self.image = PhotoImage(file=filename)
