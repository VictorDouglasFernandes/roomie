from tkinter import *

from app.commons.colors.colors import *
from app.commons.fonts.fonts import jasmineUPC8


class DefaultLabelOptionsMenu:
    def __init__(self,
                 master,
                 text,
                 clicked,
                 options=["Sim", "Não"],
                 rely=0.2,
                 relheight=None,
                 lrelwidth=0.35):
        self.clicked = clicked
        self.menu = OptionMenu(master, clicked, *options)
        self.menu.config(bg=kYellow)
        self.menu.place(relx=0.5, rely=rely, relwidth=0.35, relheight=relheight)
        self.label = Label(master, text=text, font=jasmineUPC8, bg=kWhite, fg=kYellow)
        self.label.place(relx=0.1, rely=rely, relwidth=lrelwidth)
