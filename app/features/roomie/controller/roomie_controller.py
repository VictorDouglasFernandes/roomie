from app.features.roomie.presentations.ad_roomie import AdRoomie


class RoomieController:
    def __int__(self):
        self.__roomies = []
        self.__ad_roomie = AdRoomie()

    @property
    def roomies(self):
        return self.__roomies

    def adicionar(self):
        def save_ad(self):
            price = self.current_value.get()
            living_type = self.living_type.get()  # tipo de quarto
            print(living_type)
            roommate_type = self.roommate_type.get()  # tipo de convivência
            about = self.about.get()
            is_student = self.is_student.get()
            is_smoker = self.is_smoker.get()
            has_pets = self.has_pets.get()
            has_children = self.has_children.get()
            has_job = self.has_job.get()

            print(
                "Saving roomie: About={}, Is Student={}, Is Smoker={}, Has Pets={}, Has Children={}, Has Job={}, "
                "Price={}, Living Type={}, Roommate Type={}".format(
                    about, is_student, is_smoker, has_pets, has_children, has_job, price, living_type, roommate_type))

            # saída obtida: Saving roomie: About=a, Is Student=Não, Is Smoker=Não, Has Pets=Não
            # Has Children=Não, Has Job=Não, Price=2888.0, Living Type=Compartilhado, Roommate Type=Regular

            roomie = Roomie(price=price, share_date=123, active=True, roommate_type=roommate_type,
                            living_type=living_type, about=about, is_student=is_student, is_smoker=is_smoker,
                            has_pets=has_pets, has_children=has_children, has_job=has_job)

            print(roomie)
            # saída obtida: <app.features.roomie.entities.roomie.Roomie object at 0x000002316DF5C4C0>

    def alterar(self):
        pass

    def excluir(self):
        pass

    def listar(self):
        pass
