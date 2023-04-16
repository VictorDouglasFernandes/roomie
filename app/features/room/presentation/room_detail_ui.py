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

        self.rent = LabelDetail(self.frame_1, "Valor do\naluguel (mensal)", room.price, rely=0.1)

        self.expenses = LabelDetail(self.frame_1, "Valor das\ndespesas mensais\n(água, luz,\ninternet, gás, etc.)",
                                    room.extra, rely=0.2)

        self.type = LabelDetail(self.frame_1, "Tipo do\nquarto", room.type, rely=0.4)

        self.roommates = LabelDetailColumn(self.frame_1, "*N° de moradores\ndo imóvel", room.roommates, rely=0.5)

        self.rooms = LabelDetailColumn(self.frame_1, "*N° de quartos\ndo imóvel", room.rooms, rely=0.5, relx=0.33)

        self.bathrooms = LabelDetailColumn(self.frame_1, "*N° de banheiros\ndo imóvel", room.bathrooms, rely=0.5, relx=0.69)

        self.images = TripleImageRow(self.frame_1, room.images, rely=0.8)

        self.valueBefore = LabelDetail(self.frame_2, "Exige\ncaução?", room.advance, rely=0)

        self.smoker = LabelDetail(self.frame_2, "Aceita\nfumante?", room.smoker, rely=0.1)

        self.pet = LabelDetail(self.frame_2, "Aceita\npets?", room.pets, rely=0.2)

        self.children = LabelDetail(self.frame_2, "Aceita\ncrianças?", room.children, rely=0.3)

        self.close = LabelDetail(self.frame_2, "Condomínio\nfechado?", room.condominium, rely=0.4)

        self.garage = LabelDetail(self.frame_2, "Vaga para\ngaragem?", room.garage, rely=0.5)

        self.gym = LabelDetail(self.frame_2, "Academia?", room.gym, rely=0.6)

        self.support24h = LabelDetail(self.frame_2, "Portaria 24\nhoras?", room.lobby, rely=0.7)

        self.pool = LabelDetail(self.frame_2, "Piscina?", room.pool, rely=0.8)

        self.partyRoom = LabelDetail(self.frame_2, "Salão de\nfestas?", room.party_room, rely=0.9)
