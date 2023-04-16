from tkinter import *

from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.commons.ui.default_single_frame import DefaultSingleFrame


class ListRoom:
    def __init__(self, rooms=None):
        self.rooms = rooms
        self.navigation = None
        self.selected_id = None
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
            print(self.rooms[self.listbox.curselection()[0]])
            self.selected_id = self.listbox.curselection()[0]
            self.navigation = Navigation.GET
            self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

    def scrollbox(self):
        def on_item_selected(event):
            print(self.listbox.curselection())
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.place(relx=0.9, rely=0.2, relwidth=0.05, relheight=0.6)

        self.listbox = Listbox(self.frame, bg=kYellow)
        self.listbox.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)
        for room in self.rooms:
            self.listbox.insert(END, f"{room.district} {room.price}")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", on_item_selected)
        self.scrollbar.config(command=self.listbox.yview)
