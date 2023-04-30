from app.commons.navigation import Navigation
from app.commons.ui.default_frame import *
from app.features.user.entities.user import *

class UserAds:
    def __init__(self):
        self.raiz = Tk()
        self.navigation = None
        self.user = User()
        self.tela()
        self.botoes()
        self.labels()
        self.raiz.mainloop()

    def tela(self):
        self.base = DefaultFrame(self.raiz, "Meus anúncios")
        self.frame_1 = Frame(self.raiz, bd=4, bg=kWhite)
        self.frame_1.place(relx=0.1, rely=0.1, relheight=0.80, relwidth=0.9)

    def botoes(self):
        self.bt_gerenciar_anuncio = Button(self.frame_1, text="GERENCIAR \n ANÚNCIO", fg='white', bg='#f4bc44',
                                        font=('JasmineUPC', 10), command=self.manage_ad)
        self.bt_gerenciar_anuncio.place(relx=0.43, rely=0.15, relwidth=0.15, relheight=0.08)

        self.bt_gerenciar_anuncio = Button(self.frame_1, text="STATUS DO \n ANÚNCIO", fg='white', bg='#f4bc44',
                                           font=('JasmineUPC', 10), command=self.manage_ad)
        self.bt_gerenciar_anuncio.place(relx=0.63, rely=0.15, relwidth=0.15, relheight=0.08)

        self.bt_voltar = Button(self.frame_1, text="VOLTAR", fg='white', bg='#f4bc44',
                                font=('JasmineUPC', 10), command=self.back)
        self.bt_voltar.place(relx=0.28, rely=0.90, relwidth=0.30, relheight=0.10)

    def labels(self):
        self.lb_titulo_anuncio = Label(self.frame_1, text="Anúncio 1", font=('JasmineUPC', 15), bg='#fff',
                                       fg='#f4bc44')
        self.lb_titulo_anuncio.place(relx=0, rely=0.15, relwidth=0.20, relheight=0.08)

        self.lb_tipo_anuncio = Label(self.frame_1, text="Tipo do \n anúncio", font=('JasmineUPC', 15), bg='#fff',
                                     fg='#f4bc44')
        self.lb_tipo_anuncio.place(relx=0.20, rely=0.15, relwidth=0.20, relheight=0.08)

        self.lb_status_anuncio = Label(self.frame_1, text="Ativo", font=('JasmineUPC', 12), bg='#fff',
                                     fg='#f4bc44')
        self.lb_status_anuncio.place(relx=0.80, rely=0.15, relwidth=0.05, relheight=0.08)

    def manage_ad(self):
        self.navigation = Navigation.GET
        self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()
