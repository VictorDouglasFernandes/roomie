from tkinter import *
from datetime import datetime

from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.features.roomie.entities.roomie import Roomie
from app.features.roomie.presentations.roomie_detail_ui import RoomieDetailUI


class RoomieAdPage:
    def __init__(self, roomie=None):
        self.raiz = Tk()
        self.navigation = None
        self.ui = RoomieDetailUI(self.raiz, roomie)

        self.back_button = Button(self.ui.base.bottom_frame, text="VOLTAR", bg=kYellow, fg=kWhite, command=self.back)
        self.back_button.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

        self.raiz.mainloop()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()
