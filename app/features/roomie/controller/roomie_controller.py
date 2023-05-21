from app.commons.navigation import Navigation
from app.features.roomie.entities.roomie import Roomie
from app.features.roomie.presentations.ad_roomie import AdRoomie
from app.features.roomie.presentations.edit_roomie import EditRoomie
from app.features.roomie.presentations.list_roomie import ListRoomie
from app.features.roomie.presentations.roomie_ad_page import RoomieAdPage
from app.features.roomie.presentations.roomie_detail_page import RoomieDetailPage
from app.features.roomie.repository.roomie_db import RoomieDB
from datetime import datetime


class RoomieController:
    def __init__(self, user_controller=None):
        self.dao = RoomieDB()
        self.user_controller = user_controller

    @property
    def roomies(self):
        return list(self.dao.get_all())

    @property
    def user(self):
        return self.user_controller.user

    @property
    def user_roomie(self):
        for roomie in self.roomies:
            if roomie.email == self.user.email:
                return roomie
        return None

    def roomie_verification(self, roomie: Roomie):
        _list = []
        if roomie.picture is None or len(roomie.picture) == 0:
            _list.append('imagem')
        if roomie.roommate_type is None or roomie.roommate_type == "":
            _list.append('tipo do quarto')
        if roomie.living_type is None or roomie.living_type == "":
            _list.append('tipo de convivência')
        if roomie.price is None:
            _list.append('aluguel')

        return _list

    def adicionar(self, roomie: Roomie):
        roomie.email = self.user.email
        self.user_controller.update_user(self.user)
        self.dao.add(roomie)
        # Atualizar do usuário

    def alterar(self, roomie: Roomie):
        self.adicionar(roomie)

    def excluir(self, roomie: Roomie):
        self.user.roommate_ad = None
        self.dao.remove(roomie.id)
        # Atualizar do usuário

    def show_ad_roomie(self):
        page = AdRoomie(self, self.user.email)
        if page.navigation == Navigation.POST:
            self.adicionar(page.roomie)
            return page.navigation
        elif page.navigation == Navigation.BACK:
            return page.navigation

    def show_list_roomie(self):
        page = ListRoomie(self.roomies)
        if page.navigation == Navigation.GET:
            roomie = self.roomies[page.selected_id]
            return self.show_roomie_ad_page(roomie)
        elif page.navigation == Navigation.BACK:
            return page.navigation

    def show_roomie_ad_page(self, roomie):
        page = RoomieAdPage(roomie)
        if page.navigation == Navigation.BACK:
            return self.show_list_roomie()

    def show_roomie_detail_page(self, roomie):
        page = RoomieDetailPage()
        if page.navigation == Navigation.PUT:
            self.show_edit_roomie(roomie)
        elif page.navigation == Navigation.PUT or page.navigation == Navigation.BACK:
            if page.navigation == Navigation.DELETE:
                self.excluir(roomie)
            pass

    def show_edit_roomie(self, roomie):
        page = EditRoomie(self, roomie)
        if page.navigation == Navigation.PUT:
            page.roomie.share_date = datetime.now()
            self.alterar(page.roomie)
            self.show_roomie_detail_page(page.roomie)
        elif page.navigation == Navigation.BACK:
            self.show_roomie_detail_page(roomie)


#controller = RoomieController()
#controller.show_ad_roomie()
