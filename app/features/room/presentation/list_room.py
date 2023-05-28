from tkinter import *

from app.commons.colors.colors import *
from app.commons.navigation import Navigation
from app.commons.ui.default_label_options_menu import DefaultLabelOptionsMenu
from app.commons.ui.default_single_frame import DefaultSingleFrame


class ListRoom:
    def __init__(self, rooms=None):
        self.rooms = rooms
        self.navigation = None
        self.selected_id = None
        self.raiz = Tk()
        self.base = DefaultSingleFrame(self.raiz, title="QUARTOS DISPONÍVEIS")
        self.frame = self.base.frame

        self.scrollbox()

        self.button1 = Button(self.frame, text='VISUALIZAR\nANÚNCIO\nSELECIONADO', bg=kYellow, fg=kWhite,
                              command=self.see_selected)
        self.button1.place(relx=0.25, rely=0.85, relheight=0.15, relwidth=0.2)

        self.button2 = Button(self.frame, text='VOLTAR', bg=kYellow, fg=kWhite,
                              command=self.back)
        self.button2.place(relx=0.55, rely=0.85, relheight=0.15, relwidth=0.2)

        self.filtragem()
        self.raiz.mainloop()

    def see_selected(self):
        if len(self.listbox.curselection()) > 0:
            print(self.rooms[self.listbox.curselection()[0]])
            self.selected_id = self.listbox.curselection()[0]
            self.navigation = Navigation.GET
            self.raiz.destroy()

    def back(self):
        self.navigation = Navigation.BACK
        self.raiz.destroy()

    def scrollbox(self):
        def on_item_selected(event):
            print(self.listbox.curselection())

        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.place(relx=0.9, rely=0.2, relwidth=0.05, relheight=0.6)

        self.listbox = Listbox(self.frame, bg=kYellow)
        self.listbox.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)
        for room in self.rooms:
            display_text = f"Bairro: {room.district}     " \
                           f"Valor: {room.rent_money}     " \
                           f"Data de publicação: {room.share_date}"
            self.listbox.insert(END, display_text)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", on_item_selected)
        self.scrollbar.config(command=self.listbox.yview)

    def filtragem(self):
        # Opções de preço
        price_label = Label(self.frame, text="Preço:", bg=kWhite)
        price_label.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.05)

        price_options = ["Todos", "Crescente", "Decrescente"]
        self.price_var = StringVar(self.raiz)
        self.price_var.set(price_options[0])

        price_dropdown = OptionMenu(self.frame, self.price_var, *price_options)
        price_dropdown.place(relx=0.2, rely=0.1, relwidth=0.3, relheight=0.05)

        # Opções de bairro
        district_label = Label(self.frame, text="Bairro:", bg=kWhite)
        district_label.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.05)

        district_options = ["Todos", "Trindade", "Carvoeira", "Pantanal", "Córrego Grande",
                            "Santa Mônica", "Itacorubi", "Saco dos Limões", "Serrinha"]
        self.district_var = StringVar(self.raiz)
        self.district_var.set(district_options[0])

        district_dropdown = OptionMenu(self.frame, self.district_var, *district_options)
        district_dropdown.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.05)

        # Opções de data de publicação
        date_label = Label(self.frame, text="Data:", bg=kWhite)
        date_label.place(relx=0.1, rely=0.15, relwidth=0.1, relheight=0.05)

        date_options = ["Todas", "Crescente", "Decrescente"]
        self.date_var = StringVar(self.raiz)
        self.date_var.set(date_options[0])

        date_dropdown = OptionMenu(self.frame, self.date_var, *date_options)
        date_dropdown.place(relx=0.2, rely=0.15, relwidth=0.3, relheight=0.05)

        # Botão FILTRAR
        filter_button = Button(self.frame, text="FILTRAR", bg=kYellow, command=self.filter_rooms)
        filter_button.place(relx=0.6, rely=0.15, relwidth=0.3, relheight=0.05)

    def filter_rooms(self):
        selected_price = self.price_var.get()
        selected_district = self.district_var.get()
        selected_date = self.date_var.get()

        # Aplicar filtros aos quartos
        filtered_rooms = self.rooms

        if selected_district != "Todos":
            filtered_rooms = self.filter_by_district(filtered_rooms, selected_district)

        if selected_price != "Todos":
            filtered_rooms = self.filter_by_price(filtered_rooms, selected_price)

        if selected_date != "Todas":
            filtered_rooms = self.filter_by_date(filtered_rooms, selected_date)

        if selected_price != "Todos" and selected_district != "Todos" and selected_date != "Todas":
            filtered_rooms = self.sort_all_rooms(filtered_rooms, selected_date, selected_district)

        self.filtered_rooms = filtered_rooms
        self.update_listbox()

    def filter_by_district(self, rooms, district):
        return [room for room in rooms if room.district == district]

    def filter_by_price(self, rooms, price_order):
        if price_order == "Crescente":
            return sorted(rooms, key=lambda room: room.rent_money)
        elif price_order == "Decrescente":
            return sorted(rooms, key=lambda room: room.rent_money, reverse=True)
        else:
            return rooms

    def filter_by_date(self, rooms, date_order):
        if date_order == "Crescente":
            return sorted(rooms, key=lambda room: room.share_date)
        elif date_order == "Decrescente":
            return sorted(rooms, key=lambda room: room.share_date, reverse=True)
        else:
            return rooms

    def sort_all_rooms(self, rooms, date_order, selected_district):
        if date_order == "Crescente":
            reverse_date = False
        elif date_order == "Decrescente":
            reverse_date = True


        sorted_rooms = sorted(rooms, key=lambda room: room.share_date, reverse=reverse_date)
        sorted_rooms = sorted(sorted_rooms,
                              key=lambda room: room.district if room.district != selected_district else "",
                              reverse=False)

        return sorted_rooms

    def update_listbox(self):
        self.listbox.delete(0, END)
        for room in self.filtered_rooms:
            display_text = f"Bairro: {room.district}     " \
                           f"Valor: {room.rent_money}     " \
                           f"Data de publicação: {room.share_date}"
            self.listbox.insert(END, display_text)