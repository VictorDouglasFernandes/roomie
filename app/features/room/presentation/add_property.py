from tkinter import *


class AddProperty:
    def __init__(self, master=None):
        master.title("Adicionar Anúncio de Imóvel")

        master.geometry("500x500")

        self.linha1 = Frame(master)
        self.linha1["padx"] = 10
        self.linha1["pady"] = 10
        self.linha1.pack()

        self.linha2 = Frame(master)
        self.linha2["padx"] = 10
        self.linha2["pady"] = 10
        self.linha2.pack()

        self.linha3 = Frame(master)
        self.linha3["padx"] = 10
        self.linha3["pady"] = 10
        self.linha3.pack()

        self.labelName = Label(self.linha1, text="Nome")
        self.labelName.pack(side=LEFT)

        self.entryName = Entry(self.linha1)
        self.entryName.pack(side=LEFT)

        self.labelPostalCode = Label(self.linha2, text="CEP")
        self.labelPostalCode.pack(side=LEFT)

        self.entryPostalCode = Entry(self.linha2)
        self.entryPostalCode.pack(side=LEFT)

        self.button = Button(self.linha3, text="Salvar", command=self.verify_potal_code)
        self.button.pack()

    def verify_potal_code(self):
        print(self.entryPostalCode.get())
