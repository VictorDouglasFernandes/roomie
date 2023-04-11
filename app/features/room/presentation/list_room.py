from tkinter import *

from app.commons.colors.colors import *
from app.commons.ui.default_single_frame import DefaultSingleFrame
from app.features.room.controller.room_controller import RoomController
from app.features.room.entities.room_ad import RoomAd


class ListRoom:
    def __init__(self, controller: RoomController):
        self.controller = controller
        self.raiz = Tk()
        self.base = DefaultSingleFrame(self.raiz, title="QUARTOS DISPONÍVEIS")
        self.frame = self.base.frame

        self.scrollbox()

        self.button1 = Button(self.frame, text='VISUALIZAR\nANÚNCIO\nSELECIONADO', bg=kYellow, fg=kWhite,
                              command=self.see_selected)
        self.button1.place(relx=0.25, rely=0.85, relheight=0.15, relwidth=0.2)

        self.button2 = Button(self.frame, text='VOLTAR', bg=kYellow, fg=kWhite,
                              command=self.back)
        self.button2.place(relx=0.55, rely=0.85, relheight=0.15, relwidth=0.2)

        self.raiz.mainloop()

    def see_selected(self):
        if len(self.listbox.curselection()) > 0:
            print(list(self.controller.rooms)[self.listbox.curselection()[0]])

    def back(self):
        print('back')

    def scrollbox(self):
        def on_item_selected(event):
            print(self.listbox.curselection())
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.place(relx=0.9, rely=0.2, relwidth=0.05, relheight=0.6)

        self.listbox = Listbox(self.frame, bg=kYellow)
        self.listbox.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)
        for room in self.controller.rooms:
            self.listbox.insert(END, f"{room.district} {room.price}")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", on_item_selected)
        self.scrollbar.config(command=self.listbox.yview)

controller = RoomController()
controller.dao.add(RoomAd(email='a@a.com', district='Canasvieiras', price=2000.0, extra=300.0, images=[], type= 'tipo', roommates=1, rooms=1, bathrooms=1))
ListRoom(controller)
