
from tkinter import *
from app.commons.ui.default_frame import DefaultFrame
from app.commons.ui.image_clickable import ImageClickable
from app.commons.ui.label_detail import LabelDetail, LabelDetailColumn


class RoomieDetailUI:
    def __init__(self, master=None, roomie=None):
        self.raiz = master
        self.base = DefaultFrame(self.raiz, "Anúncio de colega de quarto")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2

        self.image = ImageClickable(self.frame_1, roomie.picture)

        self.price = LabelDetail(self.frame_1, "*Valor máximo \n de aluguel mensal:", roomie.price, rely=0.2)

        self.rommate_type = LabelDetail(self.frame_1, "*Tipo de \n convivência", roomie.roommate_type, rely=0.3)

        self.is_student = LabelDetail(self.frame_1, "Estudante?",
                                    roomie.is_student, rely=0.4)

        self.is_smoker = LabelDetail(self.frame_1, "Fumante?", roomie.is_smoker, rely=0.5)

        self.has_job = LabelDetailColumn(self.frame_1, "Trabalha", roomie.has_job, rely=0.6)

        self.has_pets = LabelDetailColumn(self.frame_1, "Possui pet?", roomie.has_pets, rely=0.6, relx=0.33)

        self.has_children = LabelDetailColumn(self.frame_1, "Possui filhos?", roomie.has_children, rely=0.6, relx=0.69)

        self.about = LabelDetail(self.frame_1, "Sobre mim", roomie.about, rely=0)

