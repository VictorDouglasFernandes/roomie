from tkinter import *

from app.commons.ui.default_frame import DefaultFrame
from app.commons.ui.default_label_options_menu import DefaultLabelOptionsMenu
from app.commons.ui.image_button import ImageButton
from app.commons.ui.label_entry import LabelEntry
from app.commons.ui.label_entry_column import LabelEntryColumn


class AddRoom:
    def __init__(self, controller=None):
        self.controller = controller
        self.raiz = Tk()
        self.base = DefaultFrame(self.raiz, "Adicionar Anúncio de Imóvel")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2

        self.district_value = StringVar()
        self.district = DefaultLabelOptionsMenu(self.frame_1, "*Bairro", self.district_value, rely=0)

        self.postalCode = LabelEntry(self.frame_1, text="CEP", rely=0.1)

        self.rent = LabelEntry(self.frame_1, text="*Valor do\naluguel (mensal)", rely=0.2)

        self.expenses = LabelEntry(self.frame_1, text="*Valor das\ndespesas mensais\n(água, luz,\ninternet, gás, etc.)", rely=0.3)

        self.type_value = StringVar()
        self.type = DefaultLabelOptionsMenu(self.frame_1, "*Tipo do\nquarto", self.type_value, rely=0.5)

        self.roommates = LabelEntryColumn(self.frame_1, "*N° de moradores\ndo imóvel", rely=0.6)

        self.rooms = LabelEntryColumn(self.frame_1, "*N° de quartos\ndo imóvel", rely=0.6, relx=0.33)

        self.bathrooms = LabelEntryColumn(self.frame_1, "*N° de banheiros\ndo imóvel", rely=0.6, relx=0.69)

        self.image = ImageButton(self.frame_1, text="*Envie até 3\nfotos do imóvel")

        self.valueBefore_value = StringVar()
        self.valueBefore = DefaultLabelOptionsMenu(self.frame_2, "Exige\ncaução?", self.valueBefore_value, rely=0)

        self.smoker_value = StringVar()
        self.smoker = DefaultLabelOptionsMenu(self.frame_2, "Aceita\nfumante?", self.smoker_value, rely=0.1)

        self.pet_value = StringVar()
        self.pet = DefaultLabelOptionsMenu(self.frame_2, "Aceita\npets?", self.pet_value)

        self.children_value = StringVar()
        self.children = DefaultLabelOptionsMenu(self.frame_2, "Aceita\ncrianças?", self.children_value, rely=0.3)

        self.close_value = StringVar()
        self.close = DefaultLabelOptionsMenu(self.frame_2, "Condomínio\nfechado?", self.close_value, rely=0.4)

        self.garage_value = StringVar()
        self.garage = DefaultLabelOptionsMenu(self.frame_2, "Vaga para\ngaragem?", self.garage_value, rely=0.5)

        self.gym_value = StringVar()
        self.gym = DefaultLabelOptionsMenu(self.frame_2, "Academia?", self.gym_value, rely=0.6)

        self.support24h_value = StringVar()
        self.support24h = DefaultLabelOptionsMenu(self.frame_2, "Portaria 24\nhoras?", self.support24h_value, rely=0.7)

        self.pool_value = StringVar()
        self.pool = DefaultLabelOptionsMenu(self.frame_2, "Piscina?", self.pool_value, rely=0.8)

        self.partyRoom_value = StringVar()
        self.partyRoom = DefaultLabelOptionsMenu(self.frame_2, "Salão de\nfestas?", self.partyRoom_value, rely=0.9)

        #self.button = Button(self.linha6, text="Salvar", command=self.verify_potal_code)
        #self.button.pack()

        self.raiz.mainloop()

    def verify_potal_code(self):
        print(self.postalCode.entry.get())


AddRoom()
