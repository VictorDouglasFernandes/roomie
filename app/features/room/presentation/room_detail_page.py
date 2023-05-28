from tkinter import *

from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.features.room.presentation.room_detail_ui import RoomDetailUI


class RoomDetailPage:
    def __init__(self, room=None):
        self.raiz = Tk()
        self.navigation = None
        self.ui = RoomDetailUI(self.raiz, room=room)

        self.questions_button = Button(self.ui.base.bottom_frame, text="PERGUNTAS\nE RESPOSTAS", bg=kYellow, fg=kWhite,
                                    command=self.questions)
        self.questions_button.place(relx=0, rely=0, relheight=1, relwidth=0.2)

        self.delete_button = Button(self.ui.base.bottom_frame, text="EXCLUIR ANÚNCIO", bg=kYellow, fg=kWhite, command=self.delete)
        self.delete_button.place(relx=0.27, rely=0, relheight=1, relwidth=0.2)

        self.edit_button = Button(self.ui.base.bottom_frame, text="EDITAR ANÚNCIO", bg=kYellow, fg=kWhite, command=self.edit)
        self.edit_button.place(relx=0.53, rely=0, relheight=1, relwidth=0.2)

        self.back_button = Button(self.ui.base.bottom_frame, text="VOLTAR", bg=kYellow, fg=kWhite, command=self.back)
        self.back_button.place(relx=0.8, rely=0, relheight=1, relwidth=0.2)

        self.raiz.mainloop()

    def questions(self):
        self.navigation = Navigation.QUESTIONS
        self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

    def delete(self):
        self.navigation = Navigation.DELETE
        self.raiz.destroy()

    def edit(self):
        self.navigation = Navigation.PUT
        self.raiz.destroy()
