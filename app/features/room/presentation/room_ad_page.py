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
        self.back_button.place(relx=0.79, rely=0, relheight=1, relwidth=0.21)

        self.rating = Button(self.ui.base.bottom_frame, text="AVALIAÇÕES", bg=kYellow, fg=kWhite,
                             command=self.rating)
        self.rating.place(relx=0.26, rely=0, relheight=1, relwidth=0.21)

        if not creator:
            self.qea_button = Button(self.ui.base.bottom_frame, text="PERGUNTAS\nE RESPOSTAS", bg=kYellow, fg=kWhite,
                                     command=self.questions)
            self.qea_button.place(relx=0, rely=0, relheight=1, relwidth=0.21)

            self.interest_button = Button(self.ui.base.bottom_frame, text="TENHO\nINTERESSE", bg=kYellow, fg=kWhite,
                                          command=self.interested)
            self.interest_button.place(relx=0.52, rely=0, relheight=1, relwidth=0.21)

        self.raiz.mainloop()

    def questions(self):
        self.navigation = Navigation.QUESTIONS
        self.raiz.destroy()

    def rating(self):
        self.navigation = Navigation.RATING
        self.raiz.destroy()

    def interested(self):
        self.navigation = Navigation.INTEREST
        self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()


