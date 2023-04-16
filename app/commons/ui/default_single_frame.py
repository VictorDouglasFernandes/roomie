from tkinter import *

from app.commons.colors.colors import *
from app.commons.fonts.fonts import manrope18


class DefaultSingleFrame:
    def __init__(self, master=None, title=None):
        self.raiz = master
        self.raiz.title(title)
        self.title = Label(self.raiz, text=title.upper(), font=manrope18, bg=kWhite, fg=kYellow)
        self.title.config(anchor=CENTER)
        self.title.pack()
        self.raiz.configure(background=kWhite)  # cor do protótipo Canva
        self.raiz.geometry("800x700")  # tamanhos iniciais de tela
        self.raiz.resizable(True, True)  # se eu quero ou não que ela seja responsiva, horizontal x vertical
        self.raiz.maxsize(width=900, height=700)  # tamanhos máximos de tela
        self.raiz.minsize(width=800, height=700)

        self.frame = Frame(self.raiz, bd=4, bg=kWhite)
        self.frame.place(relx=0.1, rely=0.1, relheight=0.80, relwidth=0.8)

