from tkinter import *

from app.commons.colors.colors import *
from app.commons.fonts.fonts import jasmineUPC8


class LabelDetail:
    def __init__(self, master=None, text="- - -", detail='- - -', rely=0, relwidth=0.35):
        self.label = Label(master, text=text, font=jasmineUPC8, bg=kWhite, fg=kYellow)
        self.label.place(relx=0.1, rely=rely, relwidth=0.35)
        if detail is True:
            detail = "Sim"
        elif detail is False:
            detail = "Não"
        self.detail = Label(master, text=detail, font=jasmineUPC8, bg=kWhite, fg=kYellow)
        self.detail.place(relx=0.5, rely=rely, relwidth=relwidth)

class LabelDetailColumn:
    def __init__(self, master=None, text="- - -",  detail='- - -', rely=0, relx=0, relwidth=0.3):
        self.label = Label(master, text=text, font=jasmineUPC8, bg=kWhite, fg=kYellow)
        self.label.place(relx=relx, rely=rely, relwidth=relwidth)
        self.detail = Label(master, text=detail, font=jasmineUPC8, bg=kWhite, fg=kYellow)
        self.detail.place(relx=relx, rely=rely + 0.1, relwidth=relwidth)
