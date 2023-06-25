import tkinter
from tkinter import *

from app.commons.colors.colors import *
from app.commons.fonts.fonts import manrope18
from app.commons.navigation import Navigation
from app.commons.ui.default_single_frame import DefaultSingleFrame
from app.commons.ui.label_detail import LabelDetail
from app.features.user.presentation.login import Login
from app.features.user.presentation.user_register import UserRegister


class RoomieHomePage:
    def __init__(self, controller):
        self.navigation = None
        self.raiz = Tk()
        title = "Roomie"
        self.title = Label(self.raiz, text=title.upper(), font=manrope18, bg=kYellow, fg=kWhite)
        self.title.config(anchor=CENTER)
        self.title.pack()
        self.raiz.configure(background=kYellow)
        self.raiz.geometry("800x700")
        self.raiz.resizable(True, True)
        self.raiz.maxsize(width=900, height=700)
        self.raiz.minsize(width=800, height=700)

        self.frame = Frame(self.raiz, bd=4, bg=kYellow)
        self.frame.place(relx=0.1, rely=0.1, relheight=0.80, relwidth=0.8)
        self.controller = controller
        self.label()
        self.botoes()

        self.raiz.mainloop()


    def label(self):
        self.lb_bem_vindo = Label(self.frame, text="SEJA BEM-VINDO(A)!",
                                font=('JasmineUPC', 20), bg='#f4bc44', fg='#fff')
        self.lb_bem_vindo.place(relx=0.27, rely=0.15)
        self.lb_roomie = Label(self.frame, text="O Roomie tem como \n objetivo facilitar a busca \n por um imóvel \n "
                                                "compartilhado nos \n arredores da UFSC. \n Vamos começar?",
                                font=('JasmineUPC', 20), bg='#f4bc44', fg='#fff')
        self.lb_roomie.place(relx=0.245, rely=0.25)

    def botoes(self):
        self.bt_cadastrar = Button(self.frame, text="CADASTRAR", fg='#f4bc44', bg='#fff', font=('JasmineUPC', 11),
                                   command=self.show_register_page)
        self.bt_cadastrar.place(relx=0.345, rely=0.8, relwidth=0.3, relheight=0.08)
        self.bt_entrar = Button(self.frame, text="ENTRAR", fg='#f4bc44', bg='#fff', font=('JasmineUPC', 11),
                                command=self.show_login_page)
        self.bt_entrar.place(relx=0.345, rely=0.7, relwidth=0.3, relheight=0.08)

    def show_login_page(self):
        self.raiz.destroy()
        Login(self.controller)

    def show_register_page(self):
        self.raiz.destroy()
        UserRegister(self.controller)


# teste = RoomieHomePage()

