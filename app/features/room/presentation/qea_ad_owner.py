import tkinter
from tkinter import *
from tkinter.simpledialog import askstring

from app.commons.ui.default_frame import *
from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.commons.ui.default_single_frame import DefaultSingleFrame
from app.features.room.presentation.room_detail_ui import RoomDetailUI

class QeAAdOwner:
    def __init__(self, room, controller):
        self.controller = controller
        self.room = room
        self.raiz = Tk()
        self.navigation = None
        self.tela()
        self.create_list()

        self.bottom_frame = Frame(self.raiz, bd=4, bg=kWhite)
        self.bottom_frame.place(relx=0.1, rely=0.9, relheight=0.1, relwidth=0.8)

        self.back_button = Button(self.bottom_frame, text="VOLTAR", bg=kYellow, fg=kWhite, command=self.back)
        self.back_button.place(relx=0.35, rely=0, relheight=1, relwidth=0.3)

        self.raiz.mainloop()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

    def read_answer(self, question):
        resposta = askstring('PERGUNTAS E RESPOSTAS', 'Resposta:')
        def has_answer():
            return resposta
        if has_answer():
            if self.controller.answer_room_question(question, resposta, self.room):
                tkinter.messagebox.showwarning(title="Sucesso", message="Resposta registrada com sucesso!")
                self.update_list()
            else:
                tkinter.messagebox.showwarning(title="Erro", message="A resposta deve conter entre 3 e 200 caracteres.")

    def tela(self):
        self.base = DefaultSingleFrame(self.raiz, "Perguntas e Respostas")
        self.frame = self.base.frame

    def create_list(self):
        self.canvas = Canvas(self.frame)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        self.list_frame = Frame(self.canvas)

        self.canvas.create_window((0, 0), window=self.list_frame, anchor='nw')
        self.create_items()

    def create_items(self):
        if self.room.questions:
            for index in range(len(self.room.questions)):
                self.create_list_item(index * 2, self.room.questions[index], self.room.answers[index])

    def create_list_item(self, row, question, answer):
        text_question = question
        if len(question) > 100:
            text_question = question[:100] + '\n' + question[100:]
        if len(answer) > 100:
            answer = answer[:100] + '\n' + answer[100:]
        Label(self.list_frame, text=f"- {text_question}").grid(row=row, column=0, pady=5, padx=5)
        Label(self.list_frame, text=f"R:{answer}").grid(row=row+1, column=0, pady=5, padx=5)
        Button(self.list_frame, text="RESPONDER", bg=kYellow, fg=kWhite, command=lambda: self.read_answer(question)).grid(row=row, column=2, pady=5, padx=5)
        Button(self.list_frame, text="EXCLUIR", bg=kYellow, fg=kWhite, command=lambda: self.delete_question(question)).grid(row=row+1, column=2, pady=5, padx=5)

    def update_list(self):
        self.list_frame.destroy()
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.create_list()

    def delete_question(self, question):
        delete = self.controller.delete_ad_question(question, self.room)
        if delete:
            tkinter.messagebox.showwarning(title="Sucesso", message="Pergunta excluída com sucesso!")
        self.update_list()
