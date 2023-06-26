from app.commons.navigation import Navigation
from app.commons.ui.default_frame import *
from app.features.user.entities.user import *
from app.commons.ui.default_single_frame import DefaultSingleFrame


class UserFavoriteAds:
    def __init__(self, favorite_properties=None, controller = None):
        self.raiz = Tk()
        self.controller = controller
        self.navigation = None
        self.room = None
        self.favorite_properties = favorite_properties

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

    def tela(self):
        self.base = DefaultSingleFrame(self.raiz, "Meus Favoritos")
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
        if self.favorite_properties:
            for index in range(len(self.favorite_properties)):
                self.create_list_item(index * 2, self.favorite_properties[index])

    def create_list_item(self, row, room):
        Label(self.list_frame, text=f"Quarto {(row / 2) + 1}").grid(row=row, column=0, pady=5, padx=5)
        Button(self.list_frame, text="VISUALIZAR", bg=kYellow, fg=kWhite, command=lambda: self.see_property_ad(room)).grid(row=row, column=2, pady=5, padx=5)
        Button(self.list_frame, text="REMOVER", bg=kYellow, fg=kWhite, command=lambda: self.delete_favorite(room)).grid(row=row, column=4, pady=5, padx=5)

    def update_list(self):
        self.list_frame.destroy()
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.create_list()

    def delete_favorite(self, room):
        delete = self.controller.delete_favorite_room(room)
        if delete:
            self.favorite_properties.remove(room)
            self.update_list()

    def see_property_ad(self, room):
        self.navigation = Navigation.ROOM
        self.room = room
        self.raiz.destroy()
