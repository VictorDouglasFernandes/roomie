from fileinput import filename
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

raiz = Tk()

class Aplicacao():
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
    self.raiz.title("Anúncio de colega de quarto") #título da tela
    self.raiz.texto_inicial = Label(self.raiz, text="ANUNCIAR COLEGA DE QUARTO", font=('Manrope', 18), bg='#fff', fg='#f4bc44')
    self.raiz.texto_inicial.config(anchor=CENTER)
    self.raiz.texto_inicial.pack()
    self.raiz.configure(background='white') #cor do protótipo Canva
    self.raiz.geometry("700x500") #tamanhos iniciais de tela
    self.raiz.resizable(True, True) #se eu quero ou não que ela seja responsiva, horizontal x vertical
    self.raiz.maxsize(width=900, height=700) #tamanhos máximos de tela
    self.raiz.minsize(width=400, height=300)

  def frames(self):
    self.frame_1 = Frame(self.raiz, bd= 4, bg='white')
    self.frame_1.place(relx= 0.1, rely= 0.1, relheight= 0.80, relwidth=0.4) #1 é lado direito e 0 é esquerdo
    self.frame_2 = Frame(self.raiz, bd= 4, bg='#fff')
    self.frame_2.place(relx= 0.5, rely= 0.1, relheight= 0.80, relwidth=0.4)

  def botoes(self):

    self.bt_1 = Button(self.frame_1, text = "ENVIAR", fg='white',bg='#f4bc44',font=('JasmineUPC', 8),command=self.load_image)
    self.bt_1.place(relx=0.5, rely=0.2, relwidth=0.35, relheight=0.1)

    self.bt_2 = Button(self.frame_1, text="ANUNCIAR", bg='#f4bc44', fg='white',font=('JasmineUPC', 8))
    self.bt_2.place(relx=0.5, rely=0.92, relwidth=0.35, relheight=0.05)

    self.bt_3 = Button(self.frame_2, text = "VOLTAR", bg='#f4bc44', fg='white')
    self.bt_3.place(relx=0.5, rely=0.92, relwidth=0.35, relheight=0.05)

    ##criação de label
    self.lb_imagens = Label(self.frame_1, text="*Escolha uma\n  foto sua para \n se identificar", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
    self.lb_imagens.place(relx = 0.1, rely= 0.2, relwidth=0.35)

  def slider(self):
    self.current_value = DoubleVar()
    self.slider = Scale(self.frame_1, from_=200, to_=5000, orient='horizontal', highlightthickness=0, variable=self.current_value,
                        command=self.on_change_scale, bg ='#f4bc44', fg='white',  troughcolor='#f4bc44')
    self.slider.place(anchor='nw', relx=0.5, rely=0.4, relwidth=0.35, relheight=0.1)
    self.lb_maximo = Label(self.frame_1, text="*Valor máximo \n de aluguel mensal", font=('JasmineUPC', 8),bg='#fff', fg='#f4bc44')
    self.lb_maximo.place(relx=0.1, rely=0.4, relwidth=0.35)

  def on_change_scale(self, event):
    print(self.current_value.get())

  def dropdown(self):
    self.clicked = StringVar()
    self.drop = OptionMenu(self.frame_1, self.clicked, "Exclusivo", "Compartilhado")
    self.drop.config (bg='#f4bc44')
    self.drop.place(relx=0.5, rely=0.55, relwidth=0.35)
    self.lb_drop = Label(self.frame_1, text="*Tipo do \n quarto", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
    self.lb_drop.place(relx=0.1, rely=0.55, relwidth=0.35)

    self.drop2 = OptionMenu(self.frame_1, self.clicked, "Ocasional", "Regular", "Intensa")
    self.drop2.config (bg='#f4bc44')
    self.drop2.place(relx=0.5, rely=0.7, relwidth=0.35)
    self.lb_drop2 = Label(self.frame_1, text="*Tipo de \n convivência", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
    self.lb_drop2.place(relx=0.1, rely=0.7, relwidth=0.35)


    self.drop3 = OptionMenu(self.frame_2, self.clicked, "Sim", "Não")
    self.drop3.set="Sim"
    self.drop3.config (bg='#f4bc44')
    self.drop3.place(relx=0.5, rely=0.2, relwidth=0.35, relheight=0.05)
    self.lb_drop3 = Label(self.frame_2, text="Estudante?", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
    self.lb_drop3.place(relx=0.1, rely=0.2, relwidth=0.25)

    self.drop4 = OptionMenu(self.frame_2, self.clicked, "Sim", "Não")
    self.drop4.set="Sim"
    self.drop4.config (bg='#f4bc44')
    self.drop4.place(relx=0.5, rely=0.3, relwidth=0.35, relheight=0.05)
    self.lb_drop4 = Label(self.frame_2, text="Fumante?", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
    self.lb_drop4.place(relx=0.1, rely=0.30, relwidth=0.25,relheight=0.05)

    self.drop5 = OptionMenu(self.frame_2, self.clicked, "Sim", "Não")
    self.drop5.set="Sim"
    self.drop5.config (bg='#f4bc44')
    self.drop5.place(relx=0.5, rely=0.3, relwidth=0.35, relheight=0.05)
    self.lb_drop5 = Label(self.frame_2, text="Trabalha?", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
    self.lb_drop5.place(relx=0.1, rely=0.30, relwidth=0.25,relheight=0.05)

    self.drop6 = OptionMenu(self.frame_2, self.clicked, "Sim", "Não")
    self.drop6.set="Sim"
    self.drop6.config (bg='#f4bc44')
    self.drop6.place(relx=0.5, rely=0.4, relwidth=0.35, relheight=0.05)
    self.lb_drop6 = Label(self.frame_2, text="Possui pet?", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
    self.lb_drop6.place(relx=0.1, rely=0.40, relwidth=0.25,relheight=0.05)

    self.drop7 = OptionMenu(self.frame_2, self.clicked, "Sim", "Não")
    self.drop7.set="Sim"
    self.drop7.config (bg='#f4bc44')
    self.drop7.place(relx=0.5, rely=0.5, relwidth=0.35, relheight=0.05)
    self.lb_drop7 = Label(self.frame_2, text="Possui filhos?", font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
    self.lb_drop7.place(relx=0.1, rely=0.50, relwidth=0.25,relheight=0.05)

  def entrada(self):
    self.lb_entrada = Label(self.frame_2, text= "Me conte mais sobre você :)",font=('JasmineUPC', 8), bg='#fff', fg='#f4bc44')
    self.lb_entrada.place(relx = 0.10, rely = 0.65)

    self.entrada = Entry(self.frame_2,bg='#f4bc44', fg='white')
    self.entrada.place(relx= 0.1, rely = 0.7, relwidth= 0.75, relheight= 0.15)

  def load_image(self):
    self.filename = filedialog.askopenfilename()
    if self.filename:
      self.image = PhotoImage(file=filename)


Aplicacao()
