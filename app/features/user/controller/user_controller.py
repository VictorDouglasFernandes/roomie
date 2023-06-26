import tkinter

from app.commons.navigation import Navigation
from app.features.room.controller import room_controller
from app.features.room.presentation.interested_users_page import InterestedUsersPage
from app.features.roomie.controller import roomie_controller
from app.features.user.entities.user import User
from app.features.user.presentation.account_details import AccountDetails
from app.features.user.presentation.create_ads import CreateAds
from app.features.user.presentation.edit_account import EditAccount
from app.features.user.presentation.logged_in_home_page import LoggedInHomePage
from app.features.user.presentation.login import Login
from app.features.user.presentation.roomie_home_page import RoomieHomePage
from app.features.user.presentation.search_ads import SearchAds
from app.features.user.presentation.user_ads import UserAds
from app.features.user.presentation.user_profile import UserProfile
from app.features.user.presentation.user_register import UserRegister
from app.features.user.entities.system_grade import SystemGrade
from app.features.user.presentation.system_grade_page import SystemGradePage
from app.features.user.repository.system_grade_db import SystemGradeDB
from app.features.user.repository.user_db import UserDB


class UserController:
    def __init__(self):
        self.dao = UserDB()
        self.system_grade_dao = SystemGradeDB()
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

    def find_users_by_ids(self, ids: list):
        users = []
        if isinstance(ids, list):
            for user in self.users:
                if user.id in ids:
                    users.append(user)
        return users

    def verify_login(self, values):
        if values["user_email"] is not None and values["user_password"] is not None:
            if self.verify_email_format(values["user_email"]):
                user = self.find_user_by_id(values["user_email"])
                if isinstance(user, User) and user.password == values["user_password"]:
                    self.user = user
                    self.user.property_ad = self.room_controller.user_room
                    self.user.roommate_ad = self.roomie_controller.user_roomie
                    return True
                else:
                    tkinter.messagebox.showwarning(title="Erro", message="Credenciais inválidas.")
            else:
                tkinter.messagebox.showwarning(title="Erro", message="Digite um e-mail de formato válido.")
        else:
            tkinter.messagebox.showwarning(title="Erro", message="Por favor, preencha os campos obrigatórios.")
        return False

    def verify_email_format(self, email_adress):
        try:
            providers_list = ["hotmail", "gmail", "outlook", "live", "yahoo"]
            if "@" in email_adress and email_adress[email_adress.index("@") + 1: email_adress.index(".com")] in \
                    providers_list:
                return True
            else:
                return False
        except:
            return False

    def add_user(self, values):
        user = None
        if isinstance(values, User):
            user = values
        else:
            user = User(
                email=values['email'],
                password=values['password'],
                name=values['name'],
                surname=values['surname'],
                birthday=values['birthday'],
                cpf=values['cpf'],
                sex=values['sex'],
                cellphone_number=values['cellphone_number'],
            )

        self.dao.add(user)

    def update_user(self, user):
        self.dao.add(user)

    def delete_user(self):
        self.dao.remove(self.user.id)

    def show_login(self):
        page = Login(self)
        if page.navigation == Navigation.GET:
            for grade in self.system_grade_dao.get_all():
                if grade.email == self.user.id:
                    self.user.system_grade = grade
            self.show_logged_in_home_page()

    def show_user_register(self):
        page = UserRegister(self)
        if page.navigation == Navigation.POST:
            self.add_user(page.user)
            self.show_login()
        elif page.navigation == Navigation.BACK:
            pass

    def show_account_details(self):
        page = AccountDetails(self.user)
        if page.navigation == Navigation.PUT:
            self.show_edit_account()
        elif page.navigation == Navigation.DELETE:
            self.delete_user()
            self.show_login()
        elif page.navigation == Navigation.BACK:
            self.show_user_profile()
        elif page.navigation == Navigation.RATE:
            self.show_system_grade()

    def show_system_grade(self):
        page = SystemGradePage(self.user, self)
        if page.navigation == Navigation.BACK:
            self.show_account_details()

    def rate_system(self, user, grade):
        if user.system_grade is None:
            user.system_grade = SystemGrade(user.id, grade)
            self.system_grade_dao.add(user.system_grade)
            self.dao.add(user)
            return True
        else:
            return False

    def check_system_grade_size(self, system_grade):
        return len(system_grade) <= 200

    def show_edit_account(self):
        page = EditAccount(self)
        if page.navigation == Navigation.PUT:
            room = self.room_controller.user_room
            if room:
                self.room_controller.dao.remove(room.email)
                room.email = page.user['email']
                self.room_controller.dao.add(room)
            roomie = self.roomie_controller.user_roomie
            if roomie:
                self.roomie_controller.dao.remove(roomie.email)
                roomie.email = page.user['email']
                self.roomie_controller.dao.add(roomie)
            self.add_user(page.user)
            self.user = self.find_user_by_id(page.user['email'])
            if self.room_controller.user_room:
                self.user.property_ad = self.room_controller.user_room
            if self.roomie_controller.user_roomie:
                self.user.roommate_ad = self.roomie_controller.user_roomie
            self.show_account_details()
        elif page.navigation == Navigation.BACK:
            self.show_account_details()

    def show_logged_in_home_page(self):
        page = LoggedInHomePage()
        if page.navigation == Navigation.AD:
            self.show_create_ads()
        elif page.navigation == Navigation.LIST:
            self.show_search_ads()
        elif page.navigation == Navigation.GET:
            self.show_user_profile()
        elif page.navigation == Navigation.BACK:
            self.show_login()

    def show_roomie_home_page(self):
        RoomieHomePage(self)

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
            self.show_user_ads()
        elif page.navigation == Navigation.GET:
            self.show_account_details()
        elif page.navigation == Navigation.INTEREST:
            room_users = None
            if self.user.property_ad:
                room_users = self.find_users_by_ids(self.user.property_ad.interested_users_emails)
            self.show_interested_users(room_users)
        elif page.navigation == Navigation.BACK:
            self.show_logged_in_home_page()

    def show_interested_users(self, room_users):
        page = InterestedUsersPage(room_users)
        if page.navigation == Navigation.BACK:
            self.show_user_profile()

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

    def show_user_ads(self):
        page = UserAds(self.user, self.room_controller)
        if page.navigation == Navigation.ROOM:
            navigation = self.room_controller.show_room_detail_page(self.user.property_ad)
            if navigation is not None:
                self.show_user_ads()
        elif page.navigation == Navigation.ROOMIE:
            self.roomie_controller.show_roomie_detail_page(self.user.roommate_ad)
        elif page.navigation == Navigation.PUT:
            if page.update == Navigation.ROOM:
                pass
            elif page.update == Navigation.ROOM:
                pass
        elif page.navigation == Navigation.BACK:
            self.show_user_profile()


controller = UserController()
controller.dao.add(User(name="victor", surname="douglas", birthday="01/01/2000", sex="MALE", cpf="8888888888",
                        cellphone_number="48 999999999", email="victor@gmail.com", password="135"))
controller.dao.add(User(name="gabriel", surname="guglielmi", birthday="02/02/2000", sex="MALE", cpf="77777777777",
                        cellphone_number="48 888888888", email="gabriel@hotmail.com", password="12345"))
controller.dao.add(User(name="kamilly", surname="victoria", birthday="03/03/2000", sex="FEMALE", cpf="66666666666",
                        cellphone_number="48 777777777", email="kami@live.com", password="123"))
controller.show_login()
# controller.show_roomie_home_page()
# controller.show_user_register()
