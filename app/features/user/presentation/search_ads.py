from app.commons.navigation import Navigation
from app.commons.ui.default_frame import *


class SearchAds:
    def __init__(self):
        self.raiz = Tk()
        self.navigation = None
        self.tela()
        self.botoes()
        self.labels()
        self.raiz.mainloop()

    def tela(self):
        self.base = DefaultFrame(self.raiz, "Buscar anúncio")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2
        self.frame_3 = Frame(self.raiz, bd=4, bg=kWhite)
        self.frame_3.place(relx=0.1, rely=0.1, relheight=0.2, relwidth=0.9)

    def botoes(self):
        self.bt_buscar_anuncio = Button(self.frame_1, text="COLEGA DE QUARTO", fg='white', bg='#f4bc44',
                                        font=('JasmineUPC', 13), command=self.roomie)
        self.bt_buscar_anuncio.place(relx=0.10, rely=0.45, relwidth=0.8, relheight=0.15)

        self.bt_criar_anuncio = Button(self.frame_2, text="QUARTO", fg='white', bg='#f4bc44',
                                       font=('JasmineUPC', 13), command=self.room)
        self.bt_criar_anuncio.place(relx=0.10, rely=0.45, relwidth=0.8, relheight=0.15)

        self.bt_meu_perfil = Button(self.frame_1, text="MEU PERFIL", fg='white', bg='#f4bc44',
                                    font=('JasmineUPC', 8), command=self.my_account)
        self.bt_meu_perfil.place(relx=0.30, rely=0.80, relwidth=0.6, relheight=0.08)

        self.bt_sair = Button(self.frame_2, text="VOLTAR", fg='white', bg='#f4bc44',
                              font=('JasmineUPC', 8), command=self.back)
        self.bt_sair.place(relx=0.10, rely=0.80, relwidth=0.6, relheight=0.08)

    def labels(self):
        self.lb_mensagem = Label(self.frame_3, text="Que tipo de anúncio você \n deseja buscar?",
                                 font=('JasmineUPC', 13), bg='#fff', fg='#f4bc44')
        self.lb_mensagem.place(relx=0.27, rely=0.0, relwidth=0.35)

    def my_account(self):
        self.navigation = Navigation.GET
        self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

    def room(self):
        self.navigation = Navigation.ROOM
        self.raiz.destroy()

    def roomie(self):
        self.navigation = Navigation.ROOMIE
        self.raiz.destroy()
