import tkinter

from app.commons.navigation import Navigation
from app.features.room.controller import room_controller
from app.features.roomie.controller import roomie_controller
from app.features.user.entities.user import User
from app.features.user.presentation.create_ads import CreateAds
from app.features.user.presentation.logged_in_home_page import LoggedInHomePage
from app.features.user.presentation.login import Login
from app.features.user.presentation.search_ads import SearchAds
from app.features.user.presentation.user_profile import UserProfile
from app.features.user.repository.user_db import UserDB


class UserController:
    def __init__(self):
        self.dao = UserDB()
        self.user = None
        self.room_controller = room_controller.RoomController(self)
        self.roomie_controller = roomie_controller.RoomieController(self)

    @property
    def users(self):
        return list(self.dao.get_all())

    def find_user_by_id(self, id: str):
        for user in self.users:
            if user.id == id:
                return user

    def verify_login(self, values):
        if values["user_email"] is not None and values["user_password"] is not None:
            if self.verify_email_format(values["user_email"]):
                user = self.find_user_by_id(values["user_email"])
                if isinstance(user, User) and user.password == values["user_password"]:
                    self.user = user
                    return True
                else:
                    tkinter.messagebox.showwarning(title="Erro", message="Credenciais inválidas.")
            else:
                tkinter.messagebox.showwarning(title="Erro", message="Digite um e-mail de formato válido.")
        else:
            tkinter.messagebox.showwarning(title="Erro", message="Por favor, preencha os campos obrigatórios.")
        return False

    def verify_email_format(self, email_adress):
        providers_list = ["hotmail", "gmail", "outlook", "live", "yahoo"]
        if "@" in email_adress and email_adress[email_adress.index("@") + 1: email_adress.index(".com")] in \
                providers_list:
            return True
        else:
            return False

    def show_login(self):
        page = Login(self)
        if page.navigation == Navigation.GET:
            self.show_logged_in_home_page()

    def show_logged_in_home_page(self):
        page = LoggedInHomePage()
        if page.navigation == Navigation.AD:
            self.show_create_ads()
        elif page.navigation == Navigation.LIST:
            self.show_search_ads()
        elif page.navigation == Navigation.BACK:
            self.show_login()

    def show_create_ads(self):
        page = CreateAds()
        if page.navigation == Navigation.ROOM:
            navigation = self.room_controller.show_add_room()
            if navigation is not None:
                self.show_logged_in_home_page()
        elif page.navigation == Navigation.ROOMIE:
            navigation = self.roomie_controller.show_ad_roomie()
            if navigation is not None:
                self.show_logged_in_home_page()
        elif page.navigation == Navigation.GET:
            self.show_user_profile()
        elif page.navigation == Navigation.BACK:
            self.show_logged_in_home_page()

    def show_user_profile(self):
        page = UserProfile()
        if page.navigation == Navigation.AD:
            pass
        elif page.navigation == Navigation.GET:
            pass
        elif page.navigation == Navigation.BACK:
            self.show_logged_in_home_page()

    def show_search_ads(self):
        page = SearchAds()
        if page.navigation == Navigation.GET:
            self.show_user_profile()
        elif page.navigation == Navigation.ROOMIE:
            navigation = self.roomie_controller.show_list_roomie()
            if navigation is not None:
                self.show_search_ads()
        elif page.navigation == Navigation.ROOM:
            navigation = self.room_controller.show_list_room()
            if navigation is not None:
                self.show_search_ads()
        elif page.navigation == Navigation.BACK:
            self.show_logged_in_home_page()


controller = UserController()
controller.dao.add(User(email="victor@gmail.com", password="135"))
controller.show_login()
