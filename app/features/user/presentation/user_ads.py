from app.commons.navigation import Navigation
from app.commons.ui.default_frame import *
from app.features.user.entities.user import *


class UserAds:
    def __init__(self, user=None):
        self.raiz = Tk()
        self.navigation = None
        self.update = None
        self.user = user
        self.tela()
        self.botoes()
        if self.user.property_ad:
            self.property_label()
        if self.user.roommate_ad:
            self.roomie_label()
        self.raiz.mainloop()

    def tela(self):
        self.base = DefaultFrame(self.raiz, "Meus anúncios")
        self.frame_1 = Frame(self.raiz, bd=4, bg=kWhite)
        self.frame_1.place(relx=0.1, rely=0.1, relheight=0.80, relwidth=0.9)

    def botoes(self):
        self.bt_voltar = Button(self.frame_1, text="VOLTAR", fg='white', bg='#f4bc44',
                                font=('JasmineUPC', 10), command=self.back)
        self.bt_voltar.place(relx=0.28, rely=0.90, relwidth=0.30, relheight=0.10)

    def property_label(self):
        self.property_bt_gerenciar_anuncio = Button(self.frame_1, text="GERENCIAR \n ANÚNCIO", fg='white', bg='#f4bc44',
                                                    font=('JasmineUPC', 10), command=self.manage_property_ad)
        self.property_bt_gerenciar_anuncio.place(relx=0.43, rely=0.15, relwidth=0.15, relheight=0.08)

        self.property_bt_gerenciar_anuncio = Button(self.frame_1, text="ALTERAR STATUS DO \n ANÚNCIO", fg='white',
                                                    bg='#f4bc44', font=('JasmineUPC', 7),
                                                    command=self.property_status_switch)
        self.property_bt_gerenciar_anuncio.place(relx=0.63, rely=0.15, relwidth=0.15, relheight=0.08)

        self.property_titulo_anuncio = Label(self.frame_1, text="Anúncio Quarto", font=('JasmineUPC', 15), bg='#fff',
                                             fg='#f4bc44')
        self.property_titulo_anuncio.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.08)

        self.property_tipo_anuncio = Label(self.frame_1, text=self.user.property_ad.type, font=('JasmineUPC', 15),
                                           bg='#fff',
                                           fg='#f4bc44')
        self.property_tipo_anuncio.place(relx=0.20, rely=0.15, relwidth=0.2, relheight=0.08)

        if self.user.property_ad.active:
            self.property_status_anuncio = Label(self.frame_1, text="Ativo",
                                               font=('JasmineUPC', 12), bg='#fff', fg='#f4bc44')
        else:
            self.property_status_anuncio = Label(self.frame_1, text="Inativo",
                                               font=('JasmineUPC', 12), bg='#fff', fg='grey')
        self.property_status_anuncio.place(relx=0.80, rely=0.15, relwidth=0.2, relheight=0.08)

    def roomie_label(self):
        self.roomie_bt_gerenciar_anuncio = Button(self.frame_1, text="GERENCIAR \n ANÚNCIO", fg='white', bg='#f4bc44',
                                                  font=('JasmineUPC', 10), command=self.manage_roomie_ad)
        self.roomie_bt_gerenciar_anuncio.place(relx=0.43, rely=0.35, relwidth=0.15, relheight=0.08)

        self.roomie_bt_gerenciar_anuncio = Button(self.frame_1, text="ALTERAR STATUS DO \n ANÚNCIO", fg='white',
                                                  bg='#f4bc44', font=('JasmineUPC', 7),
                                                  command=self.roomie_status_switch)
        self.roomie_bt_gerenciar_anuncio.place(relx=0.63, rely=0.35, relwidth=0.15, relheight=0.08)

        self.roomie_titulo_anuncio = Label(self.frame_1, text="Anúncio Colega", font=('JasmineUPC', 15), bg='#fff',
                                           fg='#f4bc44')
        self.roomie_titulo_anuncio.place(relx=0, rely=0.35, relwidth=0.2, relheight=0.08)

        self.roomie_tipo_anuncio = Label(self.frame_1, text=self.user.roommate_ad.roommate_type,
                                         font=('JasmineUPC', 15), bg='#fff',
                                         fg='#f4bc44')
        self.roomie_tipo_anuncio.place(relx=0.20, rely=0.35, relwidth=0.2, relheight=0.08)

        if self.user.roommate_ad.active:
            self.roomie_status_anuncio = Label(self.frame_1, text="Ativo",
                                               font=('JasmineUPC', 12), bg='#fff', fg='#f4bc44')
        else:
            self.roomie_status_anuncio = Label(self.frame_1, text="Inativo",
                                               font=('JasmineUPC', 12), bg='#fff', fg='grey')
        self.roomie_status_anuncio.place(relx=0.80, rely=0.35, relwidth=0.2, relheight=0.08)

    def manage_property_ad(self):
        self.navigation = Navigation.ROOM
        self.raiz.destroy()

    def manage_roomie_ad(self):
        self.navigation = Navigation.ROOMIE
        self.raiz.destroy()

    # def status_property_ad(self):
    #     self.navigation = Navigation.PUT
    #     self.update = Navigation.ROOM
    #     self.raiz.destroy()
    #
    # def status_roomie_ad(self):
    #     self.navigation = Navigation.PUT
    #     self.update = Navigation.ROOMIE
    #     self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

    def property_status_switch(self):
        status = self.property_status_anuncio["text"]
        if status == "Ativo":
            self.property_status_anuncio.config(text="Inativo", fg='grey')
            self.user.property_ad.active = False
        else:
            self.property_status_anuncio.config(text="Ativo", fg='#f4bc44')
            self.user.property_ad.active = True

    def roomie_status_switch(self):
        status = self.roomie_status_anuncio["text"]
        if status == "Ativo":
            self.roomie_status_anuncio.config(text="Inativo", fg='grey')
            self.user.roommate_ad.active = False
        else:
            self.roomie_status_anuncio.config(text="Ativo", fg='#f4bc44')
            self.user.roommate_ad.active = True

