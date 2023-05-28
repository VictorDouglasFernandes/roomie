from app.commons.navigation import Navigation
from app.commons.ui.default_frame import *

class UserProfile:
    def __init__(self):
        self.raiz = Tk()
        self.navigation = None
        self.tela()
        self.botoes()
        self.raiz.mainloop()

    def tela(self):
        self.base = DefaultFrame(self.raiz, "Meu perfil")
        self.frame_1 = Frame(self.raiz, bd=4, bg=kWhite)
        self.frame_1.place(relx=0.1, rely=0.1, relheight=0.80, relwidth=0.9)

    def botoes(self):
        self.bt_minha_conta = Button(self.frame_1, text="MINHA CONTA", fg='white', bg='#f4bc44',
                                        font=('JasmineUPC', 10), command=self.my_account)
        self.bt_minha_conta.place(relx=0.26, rely=0.15, relwidth=0.35, relheight=0.10)

        self.bt_meus_anuncios = Button(self.frame_1, text="MEUS ANÚNCIOS", fg='white', bg='#f4bc44',
                                     font=('JasmineUPC', 10), command=self.ads)
        self.bt_meus_anuncios.place(relx=0.26, rely=0.30, relwidth=0.35, relheight=0.10)

        self.bt_meus_favoritos = Button(self.frame_1, text="MEUS FAVORITOS", fg='white', bg='#f4bc44',
                                     font=('JasmineUPC', 10))
        self.bt_meus_favoritos.place(relx=0.26, rely=0.45, relwidth=0.35, relheight=0.10)

        self.bt_interessados = Button(self.frame_1, text="INTERESSADOS", fg='white', bg='#f4bc44',
                                     font=('JasmineUPC', 10))
        self.bt_interessados.place(relx=0.26, rely=0.60, relwidth=0.35, relheight=0.10)

        self.bt_voltar = Button(self.frame_1, text="VOLTAR", fg='white', bg='#f4bc44',
                                      font=('JasmineUPC', 10), command=self.back)
        self.bt_voltar.place(relx=0.28, rely=0.90, relwidth=0.30, relheight=0.10)

    def my_account(self):
        self.navigation = Navigation.GET
        self.raiz.destroy()

    def ads(self):
        self.navigation = Navigation.AD
        self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

#UserProfile()
