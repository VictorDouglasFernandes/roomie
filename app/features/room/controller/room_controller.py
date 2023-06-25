from tkinter.messagebox import askyesno

from app.commons.navigation import Navigation
from app.commons.utils.parse import *
from datetime import datetime
from app.features.room.entities.property_ad import PropertyAd
from app.features.room.presentation.add_room import AddRoom
from app.features.room.presentation.edit_room import EditRoom
from app.features.room.presentation.list_room import ListRoom
from app.features.room.presentation.rating import Rating
from app.features.room.presentation.room_ad_page import RoomAdPage
from app.features.room.presentation.room_detail_page import RoomDetailPage
from app.features.room.presentation.qea_user import QeAUser
from app.features.room.presentation.qea_ad_owner import QeAAdOwner
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
        def is_back(navigation):
            return navigation == Navigation.BACK
        def see_detail(navigation):
            return navigation == Navigation.GET

        page = ListRoom(self.rooms, self)
        if see_detail(page.navigation):
            room = page.filtered_rooms[page.selected_id]
            return self.show_room_ad_page(room)
        elif is_back(page.navigation):
            return page.navigation

    def filter_by_district(self, rooms, district):
        return [room for room in rooms if room.district == district]

    def filter_by_price(self, rooms, price_order):
        def not_all():
            return price_order == "Crescente" or price_order == "Decrescente"
        if not_all():
            return sorted(rooms, key=lambda room: room.rent_money, reverse=price_order != "Crescente")
        else:
            return rooms

    def filter_by_date(self, rooms, date_order):
        def not_all():
            return date_order == "Crescente" or date_order == "Decrescente"
        if not_all():
            return sorted(rooms, key=lambda room: room.share_date, reverse=date_order != "Crescente")
        else:
            return rooms

    def sort_all_rooms(self, rooms, date_order, selected_district):
        sorted_rooms = sorted(rooms, key=lambda room: room.share_date, reverse=date_order != "Crescente")
        sorted_rooms = sorted(sorted_rooms,
                              key=lambda room: room.district if room.district != selected_district else "",
                              reverse=False)

        return sorted_rooms

    def show_room_ad_page(self, room):
        def is_back(navigation):
            return navigation == Navigation.BACK
        def is_interested(navigation):
            return navigation == Navigation.INTEREST
        def not_already_interested():
            return self.user.email not in room.interested_users_emails
        def show_questions(navigation):
            return navigation == Navigation.QUESTIONS
        page = RoomAdPage(room, room.email == self.user.email)
        if is_back(page.navigation):
            return self.show_list_room()
        elif is_interested(page.navigation):
            if not_already_interested:
                room.add_interested_user_email(self.user.email)
                self.dao.add(room)
            return self.show_list_room()
        elif page.navigation == Navigation.QUESTIONS:
            self.show_questions_page(room)
        elif page.navigation == Navigation.RATING:
            self.show_rating(room)

    def show_questions_page(self, room):
        def is_back(navigation):
            return navigation == Navigation.BACK
        page = QeAUser(room, self)
        if is_back(page.navigation):
            return self.show_room_ad_page(room)

    def show_rating(self, room):
        def is_back(navigation):
            return navigation == Navigation.BACK
        page = Rating(room, self, room.email == self.user.email)
        if is_back(page.navigation):
            return self.show_room_ad_page(room)

    def show_owner_questions_page(self, room):
        def is_back(navigation):
            return navigation == Navigation.BACK
        page = QeAAdOwner(room, self)
        if is_back(page.navigation):
            self.show_room_detail_page(room)

    def show_room_detail_page(self, room):
        page = RoomDetailPage(room)
        if page.navigation == Navigation.PUT:
            self.show_edit_room(room)
        elif page.navigation == Navigation.BACK or page.navigation == Navigation.DELETE:
            if page.navigation == Navigation.DELETE:
                self.delete_ad_room(room)
            return page.navigation
        elif page.navigation == Navigation.QUESTIONS:
            self.show_owner_questions_page(room)

    def add_room_question(self, question, room):
        if self.check_question(question, room):
            room.add_question(question)
            room.add_answer("")
            self.dao.add(room)
            return True
        else:
            return False

    def add_room_rating(self, rating, room):
        if room.add_ratings is None or rating not in room.ratings:
            room.add_ratings(rating)
            self.dao.add(room)
            return True
        else:
            return False

    def answer_room_question(self, question, answer, room):
        if self.check_answer_size(answer):
            index = room.questions.index(question)
            room.answers[index] = answer
            self.dao.add(room)
            return True
        else:
            return False

    def delete_ad_question(self, question, room):
        confirmation = askyesno("Confirmação", "Deseja mesmo excluir a pergunta?")
        if question in room.questions and confirmation:
            index = room.questions.index(question)
            del room.questions[index]
            if len(room.answers) >= index:
                del room.answers[index]
            self.dao.add(room)
            return True
        else:
            return False

    def check_question(self, question, room):
        return len(question) >= 10 and len(question) <= 200 # and question not in room.questions

    def check_answer_size(self, answer):
        return len(answer) >= 3 and len(answer) <= 200
