from tkinter import *

from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.features.room.entities.room_ad import RoomAd
from app.features.room.presentation.room_detail_ui import RoomDetailUI


class RoomAdPage:
    def __init__(self, room=None):
        self.raiz = Tk()
        self.navigation = None
        self.ui = RoomDetailUI(self.raiz, room=room)

        self.back_button = Button(self.ui.base.bottom_frame, text="VOLTAR", bg=kYellow, fg=kWhite, command=self.back)
        self.back_button.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

        self.raiz.mainloop()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

#RoomAdPage(room=RoomAd(email='mail', district='distrito', images=["C:/Users/victo/Pictures/edited/IMG_1529.jpg", "C:/Users/victo/Downloads/20230315_190422.jpg",  "C:/Users/victo/Downloads/20230315_190422.jpg"], children=True, advance=False))