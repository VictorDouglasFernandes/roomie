from tkinter import *
from app.commons.colors import *


class Welcome:
    def __init__(self):
        self.raiz = Tk()
        self.navigation = None
        self.ui = DefaultSingleFrame(self.raiz, "Roomie")
        self.frame = self.ui.frame

        self.bottom_frame = Frame(self.raiz, bd=4, bg=kWhite)
        self.bottom_frame.place(relx=0.1, rely=0.9, relheight=0.1, relwidth=0.8)

        self.back_button = Button(self.bottom_frame, text="SAIR", bg=kYellow, fg=kWhite, command=self.exit)
        self.back_button.place(relx=0, rely=0, relheight=1, relwidth=0.3)

        self.back_button = Button(self.bottom_frame, text="LOGAR", bg=kYellow, fg=kWhite, command=self.create)
        self.back_button.place(relx=0.33, rely=0, relheight=1, relwidth=0.3)

        self.back_button = Button(self.bottom_frame, text="CRIAR CONTA", bg=kYellow, fg=kWhite, command=self.login)
        self.back_button.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

        self.raiz.mainloop()

    def exit(self):
        self.raiz.destroy()

    def create(self):
        self.navigation = Navigation.POST
        self.exit()

    def login(self):
        self.navigation = Navigation.GET
        self.exit()
