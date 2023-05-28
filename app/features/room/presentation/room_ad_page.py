from tkinter import *

from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.features.room.presentation.room_detail_ui import RoomDetailUI


class RoomAdPage:
    def __init__(self, room=None, creator=None):
        self.raiz = Tk()
        self.navigation = None
        self.ui = RoomDetailUI(self.raiz, room=room)

        self.back_button = Button(self.ui.base.bottom_frame, text="VOLTAR", bg=kYellow, fg=kWhite, command=self.back)
        self.back_button.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

        if not creator:
            self.qea_button = Button(self.ui.base.bottom_frame, text="PERGUNTAS E RESPOSTAS", bg=kYellow, fg=kWhite,
                                 command=self.questions)
            self.qea_button.place(relx=0.27, rely=0, relheight=1, relwidth=0.3)

        self.raiz.mainloop()

    def questions(self):
        self.navigation = Navigation.QUESTIONS
        self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()
