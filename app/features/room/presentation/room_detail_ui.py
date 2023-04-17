from tkinter import *
from PIL import Image, ImageTk

from app.commons.ui.default_frame import DefaultFrame
from app.commons.ui.label_detail import LabelDetail, LabelDetailColumn
from app.commons.ui.triple_image_row import TripleImageRow


class RoomDetailUI:
    def __init__(self, master=None, controller=None, room=None):
        self.controller = controller
        self.raiz = master
        self.base = DefaultFrame(self.raiz, "Anúncio")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2

        self.district = LabelDetail(self.frame_1, "Bairro:", room.district, rely=0)

        self.rent = LabelDetail(self.frame_1, "Valor do\naluguel (mensal)", room.rent_money, rely=0.1)

        self.expenses = LabelDetail(self.frame_1, "Valor das\ndespesas mensais\n(água, luz,\ninternet, gás, etc.)",
                                    room.expenses_money, rely=0.2)

        self.type = LabelDetail(self.frame_1, "Tipo do\nquarto", room.type, rely=0.4)

        self.residents = LabelDetailColumn(self.frame_1, "*N° de moradores\ndo imóvel", room.residents, rely=0.5)

        self.rooms = LabelDetailColumn(self.frame_1, "*N° de quartos\ndo imóvel", room.rooms, rely=0.5, relx=0.33)

        self.bathrooms = LabelDetailColumn(self.frame_1, "*N° de banheiros\ndo imóvel", room.bathrooms, rely=0.5, relx=0.69)

        self.images = TripleImageRow(self.frame_1, room.pictures, rely=0.8)

        self.valueBefore = LabelDetail(self.frame_2, "Exige\ncaução?", room.has_collateral, rely=0)

        self.accept_smoker = LabelDetail(self.frame_2, "Aceita\nfumante?", room.accept_smoker, rely=0.1)

        self.pet = LabelDetail(self.frame_2, "Aceita\npets?", room.accept_pets, rely=0.2)

        self.accept_childs = LabelDetail(self.frame_2, "Aceita\ncrianças?", room.accept_childs, rely=0.3)

        self.close = LabelDetail(self.frame_2, "Condomínio\nfechado?", room.private_condominium, rely=0.4)

        self.has_garage = LabelDetail(self.frame_2, "Vaga para\ngaragem?", room.has_garage, rely=0.5)

        self.has_gym = LabelDetail(self.frame_2, "Academia?", room.has_gym, rely=0.6)

        self.support24h = LabelDetail(self.frame_2, "Portaria 24\nhoras?", room.has_concierge, rely=0.7)

        self.has_pool = LabelDetail(self.frame_2, "Piscina?", room.has_pool, rely=0.8)

        self.partyRoom = LabelDetail(self.frame_2, "Salão de\nfestas?", room.has_party_hall, rely=0.9)
