import os
from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
from app.commons.ui.default_frame import DefaultFrame
from app.commons.ui.default_label_options_menu import DefaultLabelOptionsMenu
from app.features.roomie.entities.roomie import Roomie

raiz = Tk()


class AdRoomie:
    def __init__(self):
        self.raiz = raiz
        self.tela()
        self.botoes()
        self.slider()
        self.dropdown()
        self.entrada()
        self.raiz.mainloop()

    def tela(self):
        self.base = DefaultFrame(self.raiz, "Anúncio de colega de quarto")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2

    def botoes(self):
        self.bt_1 = Button(self.frame_1, text="ENVIAR", fg='white', bg='#f4bc44', font=('JasmineUPC', 8),
                           command=self.load_image)
        self.bt_1.place(relx=0.5, rely=0.2, relwidth=0.35, relheight=0.1)

        self.bt_2 = Button(self.frame_1, text="ANUNCIAR", bg='#f4bc44', fg='white', font=('JasmineUPC', 8),
                           command=self.save_ad)
        self.bt_2.place(relx=0.5, rely=0.92, relwidth=0.35, relheight=0.05)

        self.bt_3 = Button(self.frame_2, text="VOLTAR", bg='#f4bc44', fg='white')
        self.bt_3.place(relx=0.5, rely=0.92, relwidth=0.35, relheight=0.05)

        ##criação de label
        self.lb_imagens = Label(self.frame_1, text="*Escolha uma\n  foto sua para \n se identificar",
                                font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
        self.lb_imagens.place(relx=0.1, rely=0.2, relwidth=0.35)

    def slider(self):
        self.current_value = DoubleVar()
        self.slider = Scale(self.frame_1, from_=200, to_=5000, orient='horizontal', highlightthickness=0,
                            variable=self.current_value,
                            command=self.on_change_scale, bg='#f4bc44', fg='white', troughcolor='#f4bc44')
        self.slider.place(anchor='nw', relx=0.5, rely=0.4, relwidth=0.35, relheight=0.1)
        self.lb_maximo = Label(self.frame_1, text="*Valor máximo \n de aluguel mensal", font=('JasmineUPC', 8),
                               bg='#fff', fg='#f4bc44')
        self.lb_maximo.place(relx=0.1, rely=0.4, relwidth=0.35)

    def on_change_scale(self, event):
        print(self.current_value.get())

    def dropdown(self):
        self.living_type = StringVar()
        self.drop = DefaultLabelOptionsMenu(self.frame_1, "*Tipo do\nquarto", self.living_type,
                                            ["Exclusivo", "Compartilhado"], 0.55)

        self.roommate_type = StringVar()
        self.drop2 = DefaultLabelOptionsMenu(self.frame_1, "*Tipo de \n convivência", self.roommate_type,
                                             ["Ocasional", "Regular", "Intensa"], 0.7)

        self.is_student = StringVar()
        self.drop3 = DefaultLabelOptionsMenu(self.frame_2, "Estudante?", self.is_student, rely=0.2, relheight=0.05,
                                             lrelwidth=0.25)

        self.is_smoker = StringVar()
        self.drop4 = DefaultLabelOptionsMenu(self.frame_2, "Fumante?", self.is_smoker, rely=0.3, relheight=0.05,
                                             lrelwidth=0.25)

        self.has_job = StringVar()
        self.drop5 = DefaultLabelOptionsMenu(self.frame_2, "Trabalha?", self.has_job, rely=0.4, relheight=0.05,
                                             lrelwidth=0.25)

        self.has_pets = StringVar()
        self.drop6 = DefaultLabelOptionsMenu(self.frame_2, "Possui pet?", self.has_pets, rely=0.5, relheight=0.05,
                                             lrelwidth=0.25)

        self.has_children = StringVar()
        self.drop7 = DefaultLabelOptionsMenu(self.frame_2, "Possui filhos?", self.has_children, rely=0.6,
                                             relheight=0.05,
                                             lrelwidth=0.25)

    def entrada(self):
        self.lb_entrada = Label(self.frame_2, text="Me conte mais sobre você :)", font=('JasmineUPC', 8), bg='#fff',
                                fg='#f4bc44')
        self.lb_entrada.place(relx=0.10, rely=0.65)
        self.about = StringVar()
        self.entrada = Entry(self.frame_2, bg='#f4bc44', fg='white', textvariable=self.about)
        self.entrada.place(relx=0.1, rely=0.7, relwidth=0.75, relheight=0.15)

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
            imagem = imagem.resize((300, 300), Image.LANCZOS)

            # Criar um objeto ImageTk para exibir a imagem na janela do tkinter
            imagem_tk = ImageTk.PhotoImage(imagem)

            # Substituir o botão "Enviar" com a miniatura da imagem
            self.bt_1.config(image=imagem_tk)
            self.bt_1.image = imagem_tk

    def str_to_bool(self, value):
        if value == 'Sim':
            return True
        elif value == 'Não':
            return False

    def save_ad(self):
        price = self.current_value.get()
        living_type = self.living_type.get()  # tipo de quarto
        roommate_type = self.roommate_type.get()  # tipo de convivência
        about = self.about.get()
        is_student = self.str_to_bool(self.is_student.get())
        is_smoker = self.str_to_bool(self.is_smoker.get())
        has_pets = self.str_to_bool(self.has_pets.get())
        has_children = self.str_to_bool(self.has_children.get())
        has_job = self.str_to_bool(self.has_job.get())

        print(
            "Saving roomie: About={}, Is Student={}, Is Smoker={}, Has Pets={}, Has Children={}, Has Job={}, "
            "Price={}, Living Type={}, Roommate Type={}".format(
                about, is_student, is_smoker, has_pets, has_children, has_job, price, living_type, roommate_type))

        roomie = Roomie(price=price, share_date=123, active=True, roommate_type=roommate_type,
                        living_type=living_type, about=about, is_student=is_student, is_smoker=is_smoker,
                        has_pets=has_pets, has_children=has_children, has_job=has_job)

        print(roomie)

        # saída obtida: <app.features.roomie.entities.roomie.Roomie object at 0x000002316DF5C4C0>


AdRoomie()
