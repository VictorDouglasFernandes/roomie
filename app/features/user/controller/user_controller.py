import tkinter


class UserController:
    def __init__(self):
        self.__users = {'gabrielguglielmik@gmail.com': '123', 'fulano@email.com': '12345'}

    def verifyLogin(self, values):
        if values["user_email"] is not None and values["user_password"] is not None:
            if self.verifyEmailFormat(values["user_email"]):
                if values["user_email"] in self.__users and self.__users[values["user_email"]] == values["user_password"]:
                    print("Bem-vindo!")
                else:
                    tkinter.messagebox.showwarning(title="Erro", message="Credenciais inválidas.")
            else:
                tkinter.messagebox.showwarning(title="Erro", message="Digite um e-mail de formato válido.")
        else:
            tkinter.messagebox.showwarning(title="Erro", message="Por favor, preencha os campos obrigatórios.")

    def verifyEmailFormat(self, email_adress):
        providers_list = ["hotmail", "gmail", "outlook", "live", "yahoo"]
        if "@" in email_adress and email_adress[email_adress.index("@")+1: email_adress.index(".com")] in \
                providers_list:
            return True
        else:
            return False
