from tkinter import *
import tkinter.font as font
raiz = Tk()

class Aplicacao():
  def __init__(self):
    self.raiz = raiz
    self.tela()
    self.frames()
    self.botoes()
    self.raiz.mainloop()

  def tela(self):
    self.raiz.title("Anúncio de colega de quarto") #título da tela
    self.raiz.configure(background='white') #cor do protótipo Canva
    self.raiz.geometry("700x500") #tamanhos iniciais de tela
    self.raiz.resizable(True, True) #se eu quero ou não que ela seja responsiva, horizontal x vertical
    self.raiz.maxsize(width=900, height=700) #tamanhos máximos de tela
    self.raiz.minsize(width=400, height=300)

  def frames(self):
    self.frame_1 = Frame(self.raiz, bd= 4, bg='black')
    self.frame_1.place(relx= 0.1, rely= 0.1, relheight= 0.80, relwidth=0.4) #1 é lado direito e 0 é esquerdo
    self.frame_2 = Frame(self.raiz, bd= 4, bg='grey')
    self.frame_2.place(relx= 0.5, rely= 0.1, relheight= 0.80, relwidth=0.4)

  def botoes(self):
    myFont = font.Font(family='JasmineUPC', size=5, weight='bold')
    self.bt_1 = Button(self.frame_1, text = "ENVIAR IMAGEM", bg='#f4bc44', fg='black')
    self.bt_1['font'] = myFont
    self.bt_1.place(relx=0.5, rely=0.2, relwidth=0.35, relheight=0.1)

Aplicacao()