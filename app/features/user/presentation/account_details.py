from tkinter import *

from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.commons.ui.default_single_frame import DefaultSingleFrame
from app.commons.ui.label_detail import LabelDetail


class AccountDetails:
    def __init__(self, user):
        self.navigation = None
        self.user = user
        self.raiz = Tk()
        self.frame = DefaultSingleFrame(self.raiz, "Minha conta")

        self.ld_name = LabelDetail(self.frame.raiz, text='Nome', detail=self.user.name, rely=0.1)
        self.ld_surname = LabelDetail(self.frame.raiz, text='Sobrenome', detail=self.user.surname, rely=0.2)
        self.ld_birthday = LabelDetail(self.frame.raiz, text='Data de\nnascimento', detail=self.user.birthday, rely=0.3)
        self.ld_sex = LabelDetail(self.frame.raiz, text='Sexo', detail=self.user.sex, rely=0.4)
        self.ld_cpf = LabelDetail(self.frame.raiz, text='CPF', detail=self.user.cpf, rely=0.5)
        self.ld_cellphone = LabelDetail(self.frame.raiz, text='Celular', detail=self.user.cellphone_number, rely=0.6)
        self.ld_email = LabelDetail(self.frame.raiz, text='E-mail', detail=self.user.email, rely=0.7)
        self.ld_password = LabelDetail(self.frame.raiz, text='Senha', detail=self.user.password, rely=0.8)

        self.bottom_frame = Frame(self.raiz, bd=4, bg=kWhite)
        self.bottom_frame.place(relx=0.1, rely=0.9, relheight=0.1, relwidth=0.8)

        self.bt_edit = Button(self.bottom_frame, text="EDITAR CONTA", fg='white', bg='#f4bc44',
                              font=('JasmineUPC', 8), command=self.edit)
        self.bt_delete = Button(self.bottom_frame, text="EXCLUIR CONTA", fg='white', bg='#f4bc44',
                               font=('JasmineUPC', 8), command=self.delete)
        self.bt_rate = Button(self.bottom_frame, text="AVALIAR\nSISTEMA", fg='white', bg='#f4bc44',
                              font=('JasmineUPC', 8), command=self.rate)
        self.bt_back = Button(self.bottom_frame, text="VOLTAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8),
                              command=self.back)

        self.bt_edit.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1)
        self.bt_delete.place(relx=0.25, rely=0.0, relwidth=0.2, relheight=1)
        self.bt_rate.place(relx=0.55, rely=0.0, relwidth=0.2, relheight=1)
        self.bt_back.place(relx=0.8, rely=0.0, relwidth=0.2, relheight=1)

        self.raiz.mainloop()

    def edit(self):
        self.navigation = Navigation.PUT
        self.raiz.destroy()

    def delete(self):
        self.navigation = Navigation.DELETE
        self.raiz.destroy()

    def rate(self):
        self.navigation = Navigation.RATE
        self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()
