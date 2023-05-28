import tkinter
from tkinter import *
from tkinter.simpledialog import askstring

from app.commons.ui.default_frame import *
from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.features.room.presentation.room_detail_ui import RoomDetailUI
# from app.features.room.controller.room_controller import RoomController

class QeAAdOwner:
    def __init__(self, room=None):
        # self.__controller = controller
        self.raiz = Tk()
        self.navigation = None
        self.tela()
        self.question()
        self.answer()
        self.botoes()

        self.raiz.mainloop()

    def read_answer(self):
        resposta = askstring('PERGUNTAS E RESPOSTAS', 'Resposta:')
        if resposta:
            if self.__controller.answer_room_question(resposta):
                tkinter.messagebox.showwarning(title="Sucesso", message="Resposta registrada com sucesso!")
            else:
                tkinter.messagebox.showwarning(title="Erro", message="A resposta deve conter entre 3 e 200 caracteres.")
    def tela(self):
        self.base = DefaultFrame(self.raiz, "Perguntas e Respostas")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2

    def question(self):
        self.lb_question = Label(self.frame_1, text="-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", font=('JasmineUPC', 12), bg='#fff',
                              fg='#f4bc44', wraplength=300, justify="left")
        self.lb_question.place(relx=0, rely=0.2)

    def answer(self):
        self.lb_answer = Label(self.frame_1, text="R:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", font=('JasmineUPC', 12), bg='#fff',
                              fg='#f4bc44', wraplength=300, justify="left")
        self.lb_answer.place(relx=0, rely=0.45)

    def botoes(self):
        self.bt_excluir_pergunta = Button(self.frame_2, text="EXCLUIR PERGUNTA", fg='white', bg='#f4bc44',
                                          font=('JasmineUPC', 8))
        self.bt_excluir_pergunta.place(relx=0, rely=0.2, relwidth=0.4, relheight=0.06)
        self.bt_responder_pergunta = Button(self.frame_2, text="RESPONDER PERGUNTA", fg='white', bg='#f4bc44',
                                            font=('JasmineUPC', 8), command=self.read_answer)
        self.bt_responder_pergunta.place(relx=0.45, rely=0.2, relwidth=0.4, relheight=0.06)


# QeAAdOwner(RoomController())

