from tkinter import *

from app.features.room.presentation.room_detail_ui import RoomDetailUI
from app.commons.colors.colors import *
from app.commons.navigation import *


class FavoriteRoom:
    def __init__(self, room=None):
        self.raiz = Tk()
        self.navigation = None
        self.ui = RoomDetailUI(self.raiz, room=room)

        self.back_button = Button(self.ui.base.bottom_frame, text="VOLTAR", bg=kYellow, fg=kWhite, command=self.back)
        self.back_button.place(relx=0.8, rely=0, relheight=1, relwidth=0.2)

        self.raiz.mainloop()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()