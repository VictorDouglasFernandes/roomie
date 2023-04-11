import os
from tkinter import *
from tkinter import filedialog

import cv2
from PIL import Image, ImageTk

from app.features.roomie.entities.roomie import Roomie

raiz = Tk()


class AdRoomie:
    def __init__(self):
        self.raiz = raiz
        self.tela()
        self.frames()
        self.botoes()
        self.slider()
        self.dropdown()
        self.entrada()
        self.raiz.mainloop()

    def tela(self):
        self.raiz.title("Anúncio de colega de quarto")  # título da tela
        self.raiz.texto_inicial = Label(self.raiz, text="ANUNCIAR COLEGA DE QUARTO", font=('Manrope', 18), bg='#fff',
                                        fg='#f4bc44')
        self.raiz.texto_inicial.config(anchor=CENTER)
        self.raiz.texto_inicial.pack()
        self.raiz.configure(background='white')  # cor do protótipo Canva
        self.raiz.geometry("700x500")  # tamanhos iniciais de tela
        self.raiz.resizable(True, True)  # se eu quero ou não que ela seja responsiva, horizontal x vertical
        self.raiz.maxsize(width=900, height=700)  # tamanhos máximos de tela
        self.raiz.minsize(width=400, height=300)

    def frames(self):
        self.frame_1 = Frame(self.raiz, bd=4, bg='white')
        self.frame_1.place(relx=0.1, rely=0.1, relheight=0.80, relwidth=0.4)  # 1 é lado direito e 0 é esquerdo
        self.frame_2 = Frame(self.raiz, bd=4, bg='#fff')
        self.frame_2.place(relx=0.5, rely=0.1, relheight=0.80, relwidth=0.4)

    def botoes(self):
        # botão 1 - enviar foto de perfil
        self.bt_1 = Button(self.frame_1, text="ENVIAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8),
                           command=self.load_image)
        self.bt_1.place(relx=0.5, rely=0.2, relwidth=0.35, relheight=0.1)

        # botão 2 - enviar anúncio
        self.bt_2 = Button(self.frame_1, text="ANUNCIAR", bg='#f4bc44', fg='white', font=('JasmineUPC', 8),
                           command=self.save_ad)
        self.bt_2.place(relx=0.5, rely=0.92, relwidth=0.35, relheight=0.05)

        # botão 3 - voltar
        self.bt_3 = Button(self.frame_2, text="VOLTAR", bg='#f4bc44', fg='white')
        self.bt_3.place(relx=0.5, rely=0.92, relwidth=0.35, relheight=0.05)

        # criação de label
        self.lb_imagens = Label(self.frame_1, text="*Escolha uma\n  foto sua para \n se identificar",
                                font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
        self.lb_imagens.place(relx=0.1, rely=0.2, relwidth=0.35)

    def slider(self):
        # slider - colocar preço máximo de aluguel
        self.current_value = DoubleVar()
        self.slider = Scale(self.frame_1, from_=200, to_=5000, orient='horizontal', highlightthickness=0,
                            variable=self.current_value,
                            command=self.on_change_scale, bg='#f4bc44', fg='white', troughcolor='#f4bc44')
        self.slider.place(anchor='nw', relx=0.5, rely=0.4, relwidth=0.35, relheight=0.1)
        self.lb_maximo = Label(self.frame_1, text="*Valor máximo \n de aluguel mensal", font=('JasmineUPC', 8),
                               bg='#fff', fg='#f4bc44')
        self.lb_maximo.place(relx=0.1, rely=0.4, relwidth=0.35)

    def on_change_scale(self):
        # função para pegar o valor máximo de aluguel
        print(self.current_value.get())

    def dropdown(self):

        # dropdown 1 - tipo de quarto
        self.living_type = StringVar()
        self.drop = OptionMenu(self.frame_1, self.living_type, "Exclusivo", "Compartilhado")
        self.drop.config(bg='#f4bc44')
        self.drop.place(relx=0.5, rely=0.55, relwidth=0.35)
        self.lb_drop = Label(self.frame_1, text="*Tipo do \n quarto", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
        self.lb_drop.place(relx=0.1, rely=0.55, relwidth=0.35)

        # dropdown 2 - tipo de convivência desejada
        self.roommate_type = StringVar()
        self.drop2 = OptionMenu(self.frame_1, self.roommate_type, "Ocasional", "Regular", "Intensa")
        self.drop2.config(bg='#f4bc44')
        self.drop2.place(relx=0.5, rely=0.7, relwidth=0.35)
        self.lb_drop2 = Label(self.frame_1, text="*Tipo de \n convivência", font=('JasmineUPC', 8), bg='#fff',
                              fg='#f4bc44')
        self.lb_drop2.place(relx=0.1, rely=0.7, relwidth=0.35)

        # dropdown 3 - atributos booleanos - estudante?
        self.is_student = StringVar()
        self.drop3 = OptionMenu(self.frame_2, self.is_student, "Sim", "Não")
        self.drop3.set = "Sim"
        self.drop3.config(bg='#f4bc44')
        self.drop3.place(relx=0.5, rely=0.2, relwidth=0.35, relheight=0.05)
        self.lb_drop3 = Label(self.frame_2, text="Estudante?", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
        self.lb_drop3.place(relx=0.1, rely=0.2, relwidth=0.25)

        # dropdown 4 - atributos booleanos - fumante?
        self.is_smoker = StringVar()
        self.drop4 = OptionMenu(self.frame_2, self.is_smoker, "Sim", "Não")
        self.drop4.set = "Sim"
        self.drop4.config(bg='#f4bc44')
        self.drop4.place(relx=0.5, rely=0.60, relwidth=0.35, relheight=0.05)
        self.lb_drop4 = Label(self.frame_2, text="Fumante?", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
        self.lb_drop4.place(relx=0.1, rely=0.60, relwidth=0.25, relheight=0.05)

        # dropdown 5 - atributos booleanos - trabalha?
        self.has_job = StringVar()
        self.drop5 = OptionMenu(self.frame_2, self.has_job, "Sim", "Não")
        self.drop5.set = "Sim"
        self.drop5.config(bg='#f4bc44')
        self.drop5.place(relx=0.5, rely=0.3, relwidth=0.35, relheight=0.05)
        self.lb_drop5 = Label(self.frame_2, text="Trabalha?", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
        self.lb_drop5.place(relx=0.1, rely=0.30, relwidth=0.25, relheight=0.05)

        # dropdown 6 - atributos booleanos - pet?
        self.has_pets = StringVar()
        self.drop6 = OptionMenu(self.frame_2, self.has_pets, "Sim", "Não")
        self.drop6.set = "Sim"
        self.drop6.config(bg='#f4bc44')
        self.drop6.place(relx=0.5, rely=0.4, relwidth=0.35, relheight=0.05)
        self.lb_drop6 = Label(self.frame_2, text="Possui pet?", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
        self.lb_drop6.place(relx=0.1, rely=0.40, relwidth=0.25, relheight=0.05)

        # dropdown 7 - atributos booleanos - filhos?
        self.has_children = StringVar()
        self.drop7 = OptionMenu(self.frame_2, self.has_children, "Sim", "Não")
        self.drop7.set = "Sim"
        self.drop7.config(bg='#f4bc44')
        self.drop7.place(relx=0.5, rely=0.5, relwidth=0.35, relheight=0.05)
        self.lb_drop7 = Label(self.frame_2, text="Possui filhos?", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
        self.lb_drop7.place(relx=0.1, rely=0.50, relwidth=0.25, relheight=0.05)

    def entrada(self):
        self.about = StringVar()
        # entrada de dados do atributo "sobre". usuário pode escrever um texto sobre si mesmo
        self.lb_entrada = Label(self.frame_2, text="Me conte mais sobre você :)", font=('JasmineUPC', 8), bg='#fff',
                                fg='#f4bc44')
        self.lb_entrada.place(relx=0.10, rely=0.7)
        self.entrada = Entry(self.frame_2, bg='#f4bc44', fg='white', textvariable=self.about)
        self.entrada.place(relx=0.1, rely=0.75, relwidth=0.75, relheight=0.15)

    def load_image(self):
        # carregamento da imagem de perfil do usuário. função vinculada ao self.bt_1, da função botoes
        self.filename = filedialog.askopenfilename()
        if self.filename:
            self.image = cv2.imread(self.filename)
            directory = "imagens"
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, os.path.basename(self.filename))
            cv2.imwrite(filepath, self.image)
            imagem = Image.open(self.filename)

            # Redimensionar a imagem para que caiba na janela
            imagem = imagem.resize((300, 300), Image.ANTIALIAS)

            # Criar um objeto ImageTk para exibir a imagem na janela do tkinter
            imagem_tk = ImageTk.PhotoImage(imagem)

            # Substituir o botão "Enviar" com a miniatura da imagem
            self.bt_1.config(image=imagem_tk)
            self.bt_1.image = imagem_tk

    def save_ad(self):
        price = self.current_value.get()
        living_type = self.living_type.get()  # tipo de quarto
        roommate_type = self.roommate_type.get()  # tipo de convivência
        about = self.about.get()
        is_student = self.is_student.get()
        is_smoker = self.is_smoker.get()
        has_pets = self.has_pets.get()
        has_children = self.has_children.get()
        has_job = self.has_job.get()

        print(
            "Saving roomie: About={}, Is Student={}, Is Smoker={}, Has Pets={}, Has Children={}, Has Job={}, Price={}, Living Type={}, Roommate Type={}".format(
                about, is_student, is_smoker, has_pets, has_children, has_job, price, living_type, roommate_type))

        roomie = Roomie(price=price, share_date=123, active=True, roommate_type=roommate_type,
                        living_type=living_type, about=about, is_student=is_student, is_smoker=is_smoker,
                        has_pets=has_pets, has_children=has_children, has_job=has_job)

        print(roomie)
        # saída obtida: <app.features.roomie.entities.roomie.Roomie object at 0x000002316DF5C4C0>


AdRoomie()
