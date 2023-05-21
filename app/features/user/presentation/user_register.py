import tkinter.messagebox
import re

from app.commons.navigation import Navigation
from app.commons.ui.default_frame import *


class UserRegister:
    def __init__(self, controller):
        self.controller = controller
        self.navigation = None
        self.user = None
        self.raiz = Tk()
        self.tela()
        self.entrada()
        self.botoes()
        self.raiz.mainloop()

    def tela(self):
        self.base = DefaultFrame(self.raiz, "Criar Conta")
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
        self.bt_editar = Button(self.frame_1, text="CRIAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8),
                                command=self.create)
        self.bt_editar.place(relx=0.25, rely=0.85, relwidth=0.7, relheight=0.15)

        self.bt_sair = Button(self.frame_2, text="VOLTAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8),
                              command=self.back)
        self.bt_sair.place(relx=0, rely=0.85, relwidth=0.7, relheight=0.15)

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

    def create(self):
        if self.validate_fields():
            self.navigation = Navigation.POST
            self.user = self.get_user()
            self.raiz.destroy()

    def validate_fields(self):
        invalid_fields = []
        user = self.get_user()
        if len(user['name']) < 1:
            invalid_fields.append('nome')
        if len(user['surname']) < 1:
            invalid_fields.append('sobrenome')
        if len(user['birthday']) < 1 or re.fullmatch(re.compile(r"\d{2}\/\d{2}\/\d{4}"), user['birthday']) is None:
            invalid_fields.append('data de nascimento')
        if len(user['sex']) < 1:
            invalid_fields.append('sexo')
        if not user['cpf'].isnumeric() or re.fullmatch(re.compile(r"\d{11}"), user['cpf']) is None:
            invalid_fields.append('cpf')
        if not user['cellphone_number'].isnumeric() or len(user['cellphone_number']) < 8:
            invalid_fields.append('celular')
        if len(user['email']) < 1 or not self.controller.verify_email_format(user['email']):
            invalid_fields.append('email')
        if len(user['password']) < 1:
            invalid_fields.append('senha')

        if len(invalid_fields) > 0:
            self.showMessageError('Campos inválidos', '\n'.join(invalid_fields))

        return len(invalid_fields) < 1

    def get_user(self):
        return {
            'name': self.entrada_name.get(),
            'surname': self.entrada_surname.get(),
            'birthday': self.entrada_birthday.get(),
            'sex': self.entrada_sex.get(),
            'cpf': self.entrada_cpf.get(),
            'cellphone_number': self.entrada_cellphone.get(),
            'email': self.entrada_email.get(),
            'password': self.entrada_password.get(),
        }

    def showMessageError(self, title, message):
        tkinter.messagebox.showwarning(title=title, message=message)
