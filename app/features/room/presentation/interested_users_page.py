from tkinter import *

from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.commons.ui.default_single_frame import DefaultSingleFrame


class InterestedUsersPage:
    def __init__(self, room_users=None, roomie_users=None):
        self.navigation = None
        self.raiz = Tk()
        self.ui = DefaultSingleFrame(self.raiz, "Interessados")
        self.frame = self.ui.frame

        self.create_list()
        counter = 0

        if isinstance(room_users, list):
            for index in range(len(room_users)):
                self.create_list_item(room_users[index], row=index, is_room=True)
                counter = index

        if isinstance(roomie_users, list):
            for index in range(counter+1, len(roomie_users)):
                self.create_list_item(roomie_users[index], row=index, is_room=False)

        self.bottom_frame = Frame(self.raiz, bd=4, bg=kWhite)
        self.bottom_frame.place(relx=0.1, rely=0.9, relheight=0.1, relwidth=0.8)

        self.back_button = Button(self.bottom_frame, text="VOLTAR", bg=kYellow, fg=kWhite, command=self.back)
        self.back_button.place(relx=0.35, rely=0, relheight=1, relwidth=0.3)

        self.raiz.mainloop()

    def create_list(self):
        self.canvas = Canvas(self.frame)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        self.list_frame = Frame(self.canvas)

        self.canvas.create_window((0, 0), window=self.list_frame, anchor='nw')

    def create_list_item(self, user, row, is_room=None):
        if user.name is not None:
            Label(self.list_frame, text=user.name).grid(row=row, column=0, pady=5, padx=5)
        if user.birthday is not None:
            Label(self.list_frame, text='Idade').grid(row=row, column=2, pady=5, padx=5) # TODO
        if user.sex is not None:
            Label(self.list_frame, text=user.sex).grid(row=row, column=4, pady=5, padx=5)
        if user.cellphone_number is not None:
            Label(self.list_frame, text=user.cellphone_number).grid(row=row, column=6, pady=5, padx=5)
        if user.email is not None:
            Label(self.list_frame, text=user.email).grid(row=row, column=8, pady=5, padx=5)
        Label(self.list_frame, text=is_room and 'Quarto' or 'Colega de Quarto').grid(row=row, column=10, pady=5, padx=5)

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()
