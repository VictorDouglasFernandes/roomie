from app.commons.ui.default_frame import *

class LoggedInHomePage:
    def __init__(self):
        self.raiz = Tk()
        self.tela()
        self.botoes()
        self.raiz.mainloop()

    def tela(self):
        self.base = DefaultFrame(self.raiz, "O que você deseja fazer?")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2

    def botoes(self):
        self.bt_buscar_anuncio = Button(self.frame_1, text="BUSCAR ANÚNCIO", fg='white', bg='#f4bc44',
                                        font=('JasmineUPC', 13))
        self.bt_buscar_anuncio.place(relx=0.10, rely=0.45, relwidth=0.8, relheight=0.15)

        self.bt_criar_anuncio = Button(self.frame_2, text="CRIAR ANÚNCIO", fg='white', bg='#f4bc44',
                                        font=('JasmineUPC', 13))
        self.bt_criar_anuncio.place(relx=0.10, rely=0.45, relwidth=0.8, relheight=0.15)

        self.bt_meu_perfil = Button(self.frame_1, text="MEU PERFIL", fg='white', bg='#f4bc44',
                                       font=('JasmineUPC', 8))
        self.bt_meu_perfil.place(relx=0.30, rely=0.80, relwidth=0.6, relheight=0.08)

        self.bt_sair = Button(self.frame_2, text="SAIR", fg='white', bg='#f4bc44',
                                    font=('JasmineUPC', 8))
        self.bt_sair.place(relx=0.10, rely=0.80, relwidth=0.6, relheight=0.08)


LoggedInHomePage()
