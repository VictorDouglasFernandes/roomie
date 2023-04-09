from fileinput import filename
from tkinter import *
from tkinter import filedialog

# from PIL import ImageTk, Image
from app.commons.ui.default_frame import DefaultFrame
from app.commons.ui.default_label_options_menu import DefaultLabelOptionsMenu

raiz = Tk()


class Aplicacao():
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

        self.bt_2 = Button(self.frame_1, text="ANUNCIAR", bg='#f4bc44', fg='white', font=('JasmineUPC', 8))
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
        self.clicked = StringVar()
        self.drop = DefaultLabelOptionsMenu(self.frame_1, "*Tipo do\nquarto", self.clicked,
                                            ["Exclusivo", "Compartilhado"], 0.55)

        self.drop2 = DefaultLabelOptionsMenu(self.frame_1, "*Tipo de \n convivência", self.clicked,
                                             ["Ocasional", "Regular", "Intensa"], 0.7)

        self.drop3 = DefaultLabelOptionsMenu(self.frame_2, "Estudante?", self.clicked, rely=0.2, relheight=0.05, lrelwidth=0.25)

        self.drop4 = DefaultLabelOptionsMenu(self.frame_2, "Fumante?", self.clicked, rely=0.3, relheight=0.05,
                                             lrelwidth=0.25)

        self.drop5 = DefaultLabelOptionsMenu(self.frame_2, "Trabalha?", self.clicked, rely=0.4, relheight=0.05,
                                             lrelwidth=0.25)

        self.drop6 = DefaultLabelOptionsMenu(self.frame_2, "Possui pet?", self.clicked, rely=0.5, relheight=0.05,
                                             lrelwidth=0.25)

        self.drop7 = DefaultLabelOptionsMenu(self.frame_2, "Possui filhos?", self.clicked, rely=0.6, relheight=0.05,
                                             lrelwidth=0.25)

    def entrada(self):
        self.lb_entrada = Label(self.frame_2, text="Me conte mais sobre você :)", font=('JasmineUPC', 8), bg='#fff',
                                fg='#f4bc44')
        self.lb_entrada.place(relx=0.10, rely=0.65)

        self.entrada = Entry(self.frame_2, bg='#f4bc44', fg='white')
        self.entrada.place(relx=0.1, rely=0.7, relwidth=0.75, relheight=0.15)

    def load_image(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            self.image = PhotoImage(file=filename)


Aplicacao()
