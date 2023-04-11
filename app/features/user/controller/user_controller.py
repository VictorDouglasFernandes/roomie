import tkinter


class UserController:
    def __init__(self):
        self.__users = {'gabrielguglielmik@gmail.com': '123', 'fulano@email.com': '12345'}

    def verify_login(self, values):
        if values["user_email"] is not None and values["user_password"] is not None:
            if values["user_email"] in self.__users and self.__users[values["user_email"]] == values["user_password"]:
                print("Bem-vindo!")
            else:
                tkinter.messagebox.showwarning(title="Erro", message="Credenciais inválidas.")
