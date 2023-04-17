from app.commons.navigation import Navigation
from app.commons.utils.parse import *
from app.features.room.entities.room_ad import RoomAd
from app.features.room.presentation.add_room import AddRoom
from app.features.room.presentation.edit_room import EditRoom
from app.features.room.presentation.list_room import ListRoom
from app.features.room.presentation.room_ad_page import RoomAdPage
from app.features.room.presentation.room_detail_page import RoomDetailPage
from app.features.room.repository.room_db import RoomDB


class RoomController:
    def __init__(self):
        self.dao = RoomDB()

    @property
    def rooms(self):
        return list(self.dao.get_all())

    def ad_room_verification(self, room: RoomAd):
        _list = []
        if room.district is None or len(room.district) == 0:
            _list.append('bairro')
        if room.price is None:
            _list.append('aluguel')
        elif float_try_parse(room.price) is None:
            _list.append('aluguel inválido')
        if room.extra is None:
            _list.append('despesas')
        elif float_try_parse(room.extra) is None:
            _list.append('despesas inválido')
        if room.type is None or len(room.type) == 0:
            _list.append('tipo')
        if room.roommates is None:
            _list.append('moradores')
        elif int_try_parse(room.roommates) is None:
            _list.append('moradores inválido')
        if room.rooms is None:
            _list.append('quartos')
        elif int_try_parse(room.rooms) is None:
            _list.append('quartos inválido')
        if room.bathrooms is None:
            _list.append('banheiros')
        elif int_try_parse(room.bathrooms) is None:
            _list.append('banheiros inválido')
        if len(room.images) == 0:
            _list.append('imagem')

        return _list

    def add_ad_room(self, room: RoomAd):
        self.dao.add(room)
        # Adicionar ao usuário

    def update_ad_room(self, room: RoomAd):
        self.add_ad_room(room)
        # Atualizar do usuário

    def delete_ad_room(self, room: RoomAd):
        self.dao.remove(room.id)
        # Remover do usuário

    def show_add_room(self):
        page = AddRoom(self)
        if page.navigation == Navigation.PUT:
            self.add_ad_room(page.room)
            # Enviar para tela de seleção de que anúncio gerar
        elif page.navigation == Navigation.BACK:
            pass
            # Enviar para tela de seleção de que anúncio gerar
            # self.

    def show_edit_room(self, room):
        page = EditRoom(self, room)
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
            self.show_room_ad_page(room)
        elif page.navigation == Navigation.BACK:
            pass
            # Enviar para tela de seleção do tipo de anuncio para pesquisar
            # self.

    def show_room_ad_page(self, room):
        page = RoomAdPage(room)
        if page.navigation == Navigation.BACK:
            self.show_list_room()

    def show_room_detail_page(self, room):
        page = RoomDetailPage(room)
        if page.navigation == Navigation.PUT:
            self.show_edit_room(room)
        elif page.navigation == Navigation.BACK or page.navigation == Navigation.DELETE:
            if page.navigation == Navigation.DELETE:
                self.delete_ad_room(room)
            pass
            # Enviar para tela de seleção de que anúncio visualizar

controller = RoomController()
controller.show_list_room()
controller.dao.add(RoomAd(
    email='a@a.com',
    price=123.0,
    extra=234.0,
    images=["C:/Users/victo/PycharmProjects/roomie/app/commons/image/name.jpg"],
    district="Trindade",
    type=None,
    roommates=2,
    rooms=3,
    bathrooms=4,
    advance=True,
    smoker=True,
    pets=True,
    children=True,
    condominium=False,
    garage=False,
    gym=False,
    lobby=False,
    pool=False,
    party_room=False,
))
controller.dao.add(RoomAd(
    email='b@b.com',
    price=345.0,
    extra=456.0,
    images=[],
    district='Trindade',
    type=None,
    roommates=3,
    rooms=4,
    bathrooms=5,
    advance=False,
    smoker=False,
    pets=False,
    children=False,
    condominium=True,
    garage=True,
    gym=True,
    lobby=True,
    pool=True,
    party_room=True,
))
controller.show_room_detail_page(controller.rooms[0])
