from tkinter import *

from app.commons.colors.colors import *
from app.commons.fonts.fonts import jasmineUPC8


class LabelEntry:
    def __init__(self, master=None, text="- - -", rely=0, relwidth=0.35):
        self.label = Label(master, text=text,  font=jasmineUPC8, bg=kWhite, fg=kYellow)
        self.label.place(relx=0.1, rely=rely, relwidth=0.35)
        self.entry = Entry(master)
        self.entry.place(relx=0.5, rely=rely, relwidth=relwidth)
