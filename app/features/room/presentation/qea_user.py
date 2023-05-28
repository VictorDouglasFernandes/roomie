import tkinter
from tkinter import *
from tkinter.simpledialog import askstring

from app.commons.ui.default_frame import *
from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.commons.ui.default_single_frame import DefaultSingleFrame
from app.features.room.presentation.room_detail_ui import RoomDetailUI
# from app.features.room.controller.room_controller import RoomController

class QeAUser:
    def __init__(self, room=None, controller=None):
        self.raiz = Tk()
        self.navigation = None
        self.room = room
        self.controller = controller
        self.tela()
        self.create_list()
        if self.room.questions:
            for index in range(len(room.questions)):
                self.create_list_item(index * 2, room.questions[index], room.answers[index])

        self.bottom_frame = Frame(self.raiz, bd=4, bg=kWhite)
        self.bottom_frame.place(relx=0.1, rely=0.9, relheight=0.1, relwidth=0.8)

        self.back_button = Button(self.bottom_frame, text="PERGUNTAR", bg=kYellow, fg=kWhite, command=self.read_question)
        self.back_button.place(relx=0.0, rely=0, relheight=1, relwidth=0.3)

        self.back_button = Button(self.bottom_frame, text="VOLTAR", bg=kYellow, fg=kWhite, command=self.back)
        self.back_button.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

        self.raiz.mainloop()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

    def read_question(self):
        pergunta = askstring('PERGUNTAS E RESPOSTAS', 'Pergunta:')
        def has_question():
            return pergunta
        if has_question():
            if self.controller.add_room_question(pergunta, self.room):
                self.show_message("Sucesso", "Pergunta registrada com sucesso!")
                self.back()
            else:
                self.show_message("Erro", "A pergunta deve conter entre 10 e 200 caracteres.")

    def tela(self):
        self.base = DefaultSingleFrame(self.raiz, "Perguntas e Respostas")
        self.frame = self.base.frame

    def show_message(self, title, message):
        tkinter.messagebox.showwarning(title=title, message=message)

    def create_list(self):
        self.canvas = Canvas(self.frame)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        self.list_frame = Frame(self.canvas)

        self.canvas.create_window((0, 0), window=self.list_frame, anchor='nw')

    def create_list_item(self, row, question, answer):
        if len(question) > 100:
            question = question[:100] + '\n' + question[100:]
        if len(answer) > 100:
            answer = answer[:100] + '\n' + answer[100:]
        Label(self.list_frame, text=f"- {question}").grid(row=row, column=0, pady=5, padx=5)
        Label(self.list_frame, text=f"R:{answer}").grid(row=row+1, column=0, pady=5, padx=5)
