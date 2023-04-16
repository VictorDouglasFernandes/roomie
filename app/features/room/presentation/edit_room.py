from tkinter import *
import tkinter

from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.commons.ui.default_frame import DefaultFrame
from app.commons.ui.default_label_options_menu import DefaultLabelOptionsMenu
from app.commons.ui.image_button import ImageButton
from app.commons.ui.label_entry import LabelEntry
from app.commons.ui.label_entry_column import LabelEntryColumn
from app.features.room.entities.room_ad import RoomAd


class EditRoom:
    def __init__(self, controller, room=None):
        self.raiz = Tk()
        self.controller = controller
        self.navigation = None
        self.base = DefaultFrame(self.raiz, "Editar Anúncio de Quarto")
        self.frame_1 = self.base.frame_1
        self.frame_2 = self.base.frame_2

        self.district_value = StringVar()
        self.district = DefaultLabelOptionsMenu(self.frame_1, "*Bairro", self.district_value, rely=0)

        self.rent = LabelEntry(self.frame_1, text="*Valor do\naluguel (mensal)", rely=0.1)

        self.expenses = LabelEntry(self.frame_1, text="*Valor das\ndespesas mensais\n(água, luz,\ninternet, gás, etc.)",
                                   rely=0.2)

        self.type_value = StringVar(value=room.type)
        self.type = DefaultLabelOptionsMenu(self.frame_1, "*Tipo do\nquarto", self.type_value, rely=0.35)

        self.roommates = LabelEntryColumn(self.frame_1, "*N° de moradores\ndo imóvel", str(room.roommates), rely=0.45)

        self.rooms = LabelEntryColumn(self.frame_1, "*N° de quartos\ndo imóvel", str(room.rooms), rely=0.45, relx=0.33)

        self.bathrooms = LabelEntryColumn(self.frame_1, "*N° de banheiros\ndo imóvel", str(room.bathrooms), rely=0.45, relx=0.69)

        self.image = ImageButton(self.frame_1, text="*Envie até 3\nfotos do imóvel")

        self.valueBefore_value = StringVar(value=self.get_default_options_value(room.advance))
        self.valueBefore = DefaultLabelOptionsMenu(self.frame_2, "Exige\ncaução?", self.valueBefore_value, rely=0)

        self.smoker_value = StringVar(value=self.get_default_options_value(room.smoker))
        self.smoker = DefaultLabelOptionsMenu(self.frame_2, "Aceita\nfumante?", self.smoker_value, rely=0.1)

        self.pet_value = StringVar(value=self.get_default_options_value(room.pets))
        self.pet = DefaultLabelOptionsMenu(self.frame_2, "Aceita\npets?", self.pet_value)

        self.children_value = StringVar(value=self.get_default_options_value(room.children))
        self.children = DefaultLabelOptionsMenu(self.frame_2, "Aceita\ncrianças?", self.children_value, rely=0.3)

        self.close_value = StringVar(value=self.get_default_options_value(room.condominium))
        self.close = DefaultLabelOptionsMenu(self.frame_2, "Condomínio\nfechado?", self.close_value, rely=0.4)

        self.garage_value = StringVar(value=self.get_default_options_value(room.garage))
        self.garage = DefaultLabelOptionsMenu(self.frame_2, "Vaga para\ngaragem?", self.garage_value, rely=0.5)

        self.gym_value = StringVar(value=self.get_default_options_value(room.gym))
        self.gym = DefaultLabelOptionsMenu(self.frame_2, "Academia?", self.gym_value, rely=0.6)

        self.support24h_value = StringVar(value=self.get_default_options_value(room.lobby))
        self.support24h = DefaultLabelOptionsMenu(self.frame_2, "Portaria 24\nhoras?", self.support24h_value, rely=0.7)

        self.pool_value = StringVar(value=self.get_default_options_value(room.pool))
        self.pool = DefaultLabelOptionsMenu(self.frame_2, "Piscina?", self.pool_value, rely=0.8)

        self.partyRoom_value = StringVar(value=self.get_default_options_value(room.party_room))
        self.partyRoom = DefaultLabelOptionsMenu(self.frame_2, "Salão de\nfestas?", self.partyRoom_value, rely=0.9)

        self.edit_button = Button(self.base.bottom_frame, text="SALVAR ANÚNCIO", bg=kYellow, fg=kWhite,
                                  command=self.save)
        self.edit_button.place(relx=0.15, rely=0, relheight=1, relwidth=0.3)

        self.back_button = Button(self.base.bottom_frame, text="VOLTAR", bg=kYellow, fg=kWhite, command=self.back)
        self.back_button.place(relx=0.55, rely=0, relheight=1, relwidth=0.3)

        self.raiz.mainloop()

    def get_default_options_value(self, value):
        if value is True:
            return "Sim"
        elif value is False:
            return "Não"

    def save(self):
        self.room = self.get_room_ad()
        missing = self.controller.ad_room_verification(self.room)

        if len(missing) > 0:
            tkinter.messagebox.showwarning(title="Campos Faltando", message='\n'.join(missing))
        else:
            self.navigation = Navigation.PUT
            self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

    def get_room_ad(self):
        return RoomAd(
            email='teste',
            price=self.rent.entry.get(),
            extra=self.expenses.entry.get(),
            # images = self.,
            district=self.district_value.get(),
            type=self.type_value.get(),
            roommates=self.roommates.entry.get(),
            rooms=self.rooms.entry.get(),
            bathrooms=self.bathrooms.entry.get(),
            advance=self.str_to_bool(self.valueBefore_value.get()),
            smoker=self.str_to_bool(self.smoker_value.get()),
            pets=self.str_to_bool(self.pet_value.get()),
            children=self.str_to_bool(self.children_value.get()),
            condominium=self.str_to_bool(self.close_value.get()),
            garage=self.str_to_bool(self.garage_value.get()),
            gym=self.str_to_bool(self.gym_value.get()),
            lobby=self.str_to_bool(self.support24h_value.get()),
            pool=self.str_to_bool(self.pool_value.get()),
            party_room=self.str_to_bool(self.partyRoom_value.get()),
        )

    def str_to_bool(self, value):
        if value == 'Sim':
            return True
        elif value == 'Não':
            return False

#EditRoom(RoomAd(email='mail', district='distrito', roommates=1, images=["C:/Users/victo/Pictures/edited/IMG_1529.jpg", "C:/Users/victo/Downloads/20230315_190422.jpg",  "C:/Users/victo/Downloads/20230315_190422.jpg"], children=True, advance=False))