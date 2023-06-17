import tkinter
from tkinter import *

from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.commons.ui.default_single_frame import DefaultSingleFrame
from app.commons.ui.label_detail import LabelDetail


class SystemGrade:
    def __init__(self, user, controller=None):
        self.navigation = None
        self.user = user
        self.controller = controller
        self.raiz = Tk()
        self.frame = DefaultSingleFrame(self.raiz, "Avaliar Sistema")
        self.label()
        self.entrada()
        self.botoes()

        self.raiz.mainloop()


    def label(self):
        self.lb_avaliar = Label(self.frame.raiz, text="Como está sendo a sua \n experiência com o Roomie? \n "
                                                      "Deixe-nos uma avaliação \n de até 200 caracteres:",
                                font=('JasmineUPC', 20), bg='#fff', fg='#f4bc44')
        self.lb_avaliar.place(relx=0.27, rely=0.15)

    def entrada(self):
        self.system_grade = StringVar()
        self.entrada_system_grade = Entry(self.frame.raiz, bg='#f4bc44', fg='white', textvariable=self.system_grade)
        self.entrada_system_grade.place(relx=0.18, rely=0.4, relwidth=0.6, relheight=0.25)

    def botoes(self):
        self.bt_back = Button(self.frame.raiz, text="VOLTAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8),
                              command=self.back)
        self.bt_back.place(relx=0.58, rely=0.8, relwidth=0.2, relheight=0.08)
        self.bt_enviar = Button(self.frame.raiz, text="ENVIAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8),
                              command=self.enviar)
        self.bt_enviar.place(relx=0.18, rely=0.8, relwidth=0.2, relheight=0.08)

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

    def enviar(self):
        avaliacao = self.system_grade.get()
        def has_rate():
            return avaliacao != ""
        if has_rate():
            if self.controller.check_system_grade_size(avaliacao):
                if self.controller.rate_system(self.user, avaliacao):
                    self.show_message("Sucesso", "Avaliação enviada com sucesso!")
                    self.back()
                else:
                    self.show_message("Erro", "O usuário já enviou uma avaliação anteriormente.")
            else:
                self.show_message("Erro", "A avaliação deve possuir até 200 caracteres.")

    def show_message(self, title, message):
        tkinter.messagebox.showwarning(title=title, message=message)

