from app.features.user.presentation.login import Login

class User():
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        self.__users = {'gabrielguglielmik@gmail.com': '123', 'fulano@email.com': '12345'}
        self.login()

    def login(self):
        tela_login = Login()
        user_login_data = tela_login.enter_user_data()
        print(user_login_data["user_email"], user_login_data["user_password"])
        # if user_login_data["user_email"] != None and user_login_data["user_password"] != None:
        #    if user_login_data["user_email"] in self.__users and self.__users[user_login_data["user_email"]] == user_login_data["user_password"]:
        #        print("Bem-vindo!")
        #    else:
        #        print("Dados incorretos!")
        # else:
        #     print("Digite dados válidos")

