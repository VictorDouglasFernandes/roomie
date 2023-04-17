from tkinter import *

from app.commons.colors.colors import *
from app.commons.fonts.fonts import jasmineUPC8


class LabelEntryColumn:
    def __init__(self, master=None, text="- - -", initial_value=None, rely=0, relx=0, relwidth=0.3):
        self.label = Label(master, text=text, font=jasmineUPC8, bg=kWhite, fg=kYellow)
        self.label.place(relx=relx, rely=rely, relwidth=relwidth)
        self.entry = Entry(master)
        if isinstance(initial_value, str) and initial_value != "None":
            self.entry.insert(0, initial_value)
        self.entry.place(relx=relx, rely=rely+0.1, relwidth=relwidth)