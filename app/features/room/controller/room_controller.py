from app.commons.navigation import Navigation
from app.commons.utils.parse import *
from datetime import datetime
from app.features.room.entities.property_ad import PropertyAd
from app.features.room.presentation.add_room import AddRoom
from app.features.room.presentation.edit_room import EditRoom
from app.features.room.presentation.list_room import ListRoom
from app.features.room.presentation.room_ad_page import RoomAdPage
from app.features.room.presentation.room_detail_page import RoomDetailPage
from app.features.room.repository.room_db import RoomDB


class RoomController:
    def __init__(self, user_controller=None):
        self.dao = RoomDB()
        self.user_controller = user_controller

    @property
    def rooms(self):
        return list(self.dao.get_all())

    @property
    def user(self):
        return self.user_controller.user

    @property
    def user_room(self):
        for room in self.rooms:
            if room.email == self.user.email:
                return room
        return None

    def ad_room_verification(self, room):
        _list = []
        if room["district"] is None or len(room["district"]) == 0:
            _list.append('bairro')
        if room["rent_money"] is None:
            _list.append('aluguel')
        elif float_try_parse(room["rent_money"]) is None:
            _list.append('aluguel inválido')
        if room["expenses_money"] is None:
            _list.append('despesas')
        elif float_try_parse(room["expenses_money"]) is None:
            _list.append('despesas inválido')
        if room["type"] is None or len(room["type"]) == 0:
            _list.append('tipo')
        if room["residents"] is None:
            _list.append('moradores')
        elif int_try_parse(room["residents"]) is None:
            _list.append('moradores inválido')
        if room["rooms"] is None:
            _list.append('quartos')
        elif int_try_parse(room["rooms"]) is None:
            _list.append('quartos inválido')
        if room["bathrooms"] is None:
            _list.append('banheiros')
        elif int_try_parse(room["bathrooms"]) is None:
            _list.append('banheiros inválido')
        if len(room["pictures"]) == 0:
            _list.append('imagem')

        return _list

    def add_ad_room(self, values, update=None):
        room = PropertyAd(
            email=self.user.email,
            active=True,
            share_date=datetime.now(),
            rent_money=values["rent_money"],
            expenses_money=values["expenses_money"],
            pictures=values["pictures"],
            district=values["district"],
            type=values["type"],
            residents=values["residents"],
            rooms=values["rooms"],
            bathrooms=values["bathrooms"],
            has_collateral=values["has_collateral"],
            accept_smoker=values["accept_smoker"],
            accept_pets=values["accept_pets"],
            accept_childs=values["accept_childs"],
            private_condominium=values["private_condominium"],
            has_garage=values["has_garage"],
            has_gym=values["has_gym"],
            has_concierge=values["has_concierge"],
            has_pool=values["has_pool"],
            has_party_hall=values["has_party_hall"],
        )
        if update:
            room.share_date = values["share_date"]
            room.active = values["active"]
            room.interested_users = values["interested_users"]
        self.user.property_ad = room
        self.user_controller.update_user(self.user)
        self.dao.add(room)
        # Adicionar ao usuário

    def update_ad_room(self, room):
        self.add_ad_room(room, update=True)
        # Atualizar do usuário

    def delete_ad_room(self, room: PropertyAd):
        self.user.property_ad = None
        self.dao.remove(room.id)
        # Remover do usuário

    def show_add_room(self):
        page = AddRoom(self, self.user.email)
        if page.navigation == Navigation.PUT:
            self.add_ad_room(page.room)
            return page.navigation
        elif page.navigation == Navigation.BACK:
            return page.navigation

    def show_edit_room(self, room):
        page = EditRoom(self, room, self.user.email)
        if page.navigation == Navigation.PUT:
            self.update_ad_room(page.room)
            # Ajustar para atualizar do usuário
            self.show_room_detail_page(page.room)
        elif page.navigation == Navigation.BACK:
            self.show_room_detail_page(room)

    def show_list_room(self):
        page = ListRoom(self.rooms)
        if page.navigation == Navigation.GET:
            room = self.rooms[page.selected_id]
            return self.show_room_ad_page(room)
        elif page.navigation == Navigation.BACK:
            return page.navigation

    def show_room_ad_page(self, room):
        page = RoomAdPage(room, room.email == self.user.email)
        if page.navigation == Navigation.BACK:
            return self.show_list_room()
        elif page.navigation == Navigation.INTEREST:
            if self.user.email not in room.interested_users_emails:
                room.add_interested_user_email(self.user.email)
                self.dao.add(room)
            return self.show_list_room()

    def show_room_detail_page(self, room):
        page = RoomDetailPage(room)
        if page.navigation == Navigation.PUT:
            self.show_edit_room(room)
        elif page.navigation == Navigation.BACK or page.navigation == Navigation.DELETE:
            if page.navigation == Navigation.DELETE:
                self.delete_ad_room(room)
            return page.navigation

# controller = RoomController()
# controller.show_list_room()
# controller.dao.add(RoomAd(
#     email='a@a.com',
#     rent_money=123.0,
#     expenses_money=234.0,
#     images=["C:/Users/victo/PycharmProjects/roomie/app/commons/image/name.jpg"],
#     district="Trindade",
#     type=None,
#     residents=2,
#     rooms=3,
#     bathrooms=4,
#     has_collateral=True,
#     accept_smoker=True,
#     pets=True,
#     accept_childs=True,
#     private_condominium=False,
#     has_garage=False,
#     has_gym=False,
#     has_concierge=False,
#     has_pool=False,
#     has_party_hall=False,
# ))
# controller.dao.add(RoomAd(
#     email='b@b.com',
#     rent_money=345.0,
#     expenses_money=456.0,
#     images=[],
#     district='Trindade',
#     type=None,
#     residents=3,
#     rooms=4,
#     bathrooms=5,
#     has_collateral=False,
#     accept_smoker=False,
#     pets=False,
#     accept_childs=False,
#     private_condominium=True,
#     has_garage=True,
#     has_gym=True,
#     has_concierge=True,
#     has_pool=True,
#     has_party_hall=True,
# ))
# controller.show_room_detail_page(controller.rooms[0])
