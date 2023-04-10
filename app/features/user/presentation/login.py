from tkinter import *

from app.commons.ui.default_frame import *

raiz = Tk()

class Login:
    def __init__(self):
        self.raiz = raiz
        self.tela()
        self.entrada()
        self.botoes()
        self.raiz.mainloop()


    def tela(self):
        self.base = DefaultFrame(self.raiz, "Entrar na Conta")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2


    def entrada(self):
        self.lb_email = Label(self.frame_1, text="* E-mail", font=('JasmineUPC', 20), bg='#fff',
                              fg='#f4bc44')
        self.lb_email.place(relx=0.25, rely=0.2)
        self.entrada_email = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada_email.place(relx=0, rely=0.22, relwidth=0.7, relheight=0.06)

        self.lb_password = Label(self.frame_1, text="* Senha", font=('JasmineUPC', 20), bg='#fff',
                              fg='#f4bc44')
        self.lb_password.place(relx=0.25, rely=0.3)
        self.entrada_password = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada_password.place(relx=0, rely=0.32, relwidth=0.7, relheight=0.06)

        # self.lb_recuperar_senha = Label(self.frame_2, text="Recuperar senha", font=('JasmineUPC', 10), bg='#fff',
        #                       fg='#f4bc44')
        # self.lb_recuperar_senha.place(relx=0, rely=0.40, relwidth=0.7, relheight=0.06)


    def botoes(self):
        self.bt_entrar = Button(self.frame_1, text="ENTRAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8))
        self.bt_entrar.place(relx=0.25, rely=0.6, relwidth=0.7, relheight=0.15)

        self.bt_sair = Button(self.frame_2, text="VOLTAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8))
        self.bt_sair.place(relx=0, rely=0.6, relwidth=0.7, relheight=0.15)

        self.bt_recuperar_senha = Button(self.frame_2, text="Recuperar senha", fg='#f4bc44', bg='white', font=('JasmineUPC', 10))
        self.bt_recuperar_senha.place(relx=0.09, rely=0.4, relwidth=0.5, relheight=0.06)

Login()
