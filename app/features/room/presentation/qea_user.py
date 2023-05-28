import tkinter
from tkinter import *
from app.commons.ui.default_frame import *
from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.features.room.presentation.room_detail_ui import RoomDetailUI
# from app.features.room.controller.room_controller import RoomController

class QeAUser:
    def __init__(self, room=None, controller=None):
        self.raiz = Tk()
        self.navigation = None
        self.room = room
        self.__controller = controller
        self.tela()
        if self.room.questions:
            self.question()
        self.question()
        self.answer()
        self.entrada()
        self.botoes()

        self.raiz.mainloop()

    def read_question(self):
        pergunta = self.entrada_pergunta.get()
        if pergunta:
            if self.__controller.add_room_question(pergunta):
                self.show_message("Sucesso", "Pergunta registrada com sucesso!")
            else:
                self.show_message("Erro", "A pergunta deve conter entre 10 e 200 caracteres.")

    def tela(self):
        self.base = DefaultFrame(self.raiz, "Perguntas e Respostas")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2
        self.frame_3 = Frame(self.raiz, bd=4, bg=kWhite)
        self.frame_3.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    def question(self):
        self.lb_question = Label(self.frame_3, text="-" + self.room.questions.keys, font=('JasmineUPC', 12), bg='#fff',
                              fg='#f4bc44', wraplength=600, justify="center")
        self.lb_question.place(relx=0.025, rely=0.2)

    def answer(self):
        self.lb_answer = Label(self.frame_3, text="R:", font=('JasmineUPC', 12), bg='#fff',
                              fg='#f4bc44', wraplength=600, justify="center")
        self.lb_answer.place(relx=0.025, rely=0.3)

    def entrada(self):
        self.lb_faca_uma_pergunta = Label(self.frame_3, text="Ficou com alguma dúvida sobre o imóvel? \n Faça uma pergunta:",
                                 font=('JasmineUPC', 15), bg='#fff', fg='#f4bc44')
        self.lb_faca_uma_pergunta.place(relx=0.2, rely=0.5)
        self.fazer_pergunta = StringVar()
        self.entrada_pergunta = Entry(self.frame_3, bg='#f4bc44', fg='white', textvariable=self.fazer_pergunta)
        self.entrada_pergunta.place(relx=0.11, rely=0.6, relwidth=0.75, relheight=0.15)

    def botoes(self):
        self.bt_enviar_pergunta = Button(self.frame_3, text="ENVIAR", fg='white', bg='#f4bc44',
                                          font=('JasmineUPC', 8), command=self.read_question)
        self.bt_enviar_pergunta.place(relx=0.4, rely=0.78, relwidth=0.2, relheight=0.06)

    def show_message(self, title, message):
        tkinter.messagebox.showwarning(title=title, message=message)

# QeAUser(RoomController())
