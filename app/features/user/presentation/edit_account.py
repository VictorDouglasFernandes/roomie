import tkinter.messagebox
from app.commons.ui.default_frame import *


class EditAccount:
    def __init__(self):
        # self.__controller = controller
        self.raiz = Tk()
        self.tela()
        self.entrada()
        self.botoes()
        self.raiz.mainloop()

    def tela(self):
        self.base = DefaultFrame(self.raiz, "Editar Conta")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2

    def entrada(self):
        self.lb_name = Label(self.frame_1, text="* Nome", font=('JasmineUPC', 20), bg='#fff',
                              fg='#f4bc44')
        self.lb_name.place(relx=0.25, rely=0.0)
        self.entrada_name = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada_name.place(relx=0, rely=0.02, relwidth=0.7, relheight=0.06)

        self.lb_surname = Label(self.frame_1, text="* Sobrenome", font=('JasmineUPC', 20), bg='#fff',
                             fg='#f4bc44')
        self.lb_surname.place(relx=0.25, rely=0.1)
        self.entrada_surname = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada_surname.place(relx=0, rely=0.12, relwidth=0.7, relheight=0.06)

        self.lb_birthday = Label(self.frame_1, text="* Data de nascimento", font=('JasmineUPC', 13), bg='#fff',
                                fg='#f4bc44')
        self.lb_birthday.place(relx=0.25, rely=0.2)
        self.entrada_birthday = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada_birthday.place(relx=0, rely=0.22, relwidth=0.7, relheight=0.06)

        self.lb_sex = Label(self.frame_1, text="* Sexo", font=('JasmineUPC', 20), bg='#fff',
                                fg='#f4bc44')
        self.lb_sex.place(relx=0.25, rely=0.3)
        self.entrada_sex = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada_sex.place(relx=0, rely=0.32, relwidth=0.7, relheight=0.06)

        self.lb_cpf = Label(self.frame_1, text="* CPF", font=('JasmineUPC', 20), bg='#fff',
                                fg='#f4bc44')
        self.lb_cpf.place(relx=0.25, rely=0.4)
        self.entrada_cpf = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada_cpf.place(relx=0, rely=0.42, relwidth=0.7, relheight=0.06)

        self.lb_cellphone = Label(self.frame_1, text="* Celular", font=('JasmineUPC', 20), bg='#fff',
                                fg='#f4bc44')
        self.lb_cellphone.place(relx=0.25, rely=0.5)
        self.entrada_cellphone = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada_cellphone.place(relx=0, rely=0.52, relwidth=0.7, relheight=0.06)

        self.lb_email = Label(self.frame_1, text="* E-mail", font=('JasmineUPC', 20), bg='#fff',
                                fg='#f4bc44')
        self.lb_email.place(relx=0.25, rely=0.6)
        self.entrada_email = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada_email.place(relx=0, rely=0.62, relwidth=0.7, relheight=0.06)

        self.lb_password = Label(self.frame_1, text="* Senha", font=('JasmineUPC', 20), bg='#fff',
                                fg='#f4bc44')
        self.lb_password.place(relx=0.25, rely=0.7)
        self.entrada_password = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada_password.place(relx=0, rely=0.72, relwidth=0.7, relheight=0.06)

    def botoes(self):
        self.bt_editar = Button(self.frame_1, text="EDITAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8), command=None)
        self.bt_editar.place(relx=0.25, rely=0.85, relwidth=0.7, relheight=0.15)

        self.bt_sair = Button(self.frame_2, text="VOLTAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8))
        self.bt_sair.place(relx=0, rely=0.85, relwidth=0.7, relheight=0.15)

    def showMessageError(self, title, message):
        tkinter.messagebox.showwarning(title=title, message=message)
