from typing import Counter, final
from tabulate import tabulate
import time


# CLASS MENU
class Menu:
    def __init__(self):
        pass

    def print_menu(self):
            print("\n")
            print("                        Welcome to 'Rïf's Caribbean Social! ")
            print("                        ===================================")
            print("\n")
            # f"{my_number:,{cents}}
            self.testing = int(0)
            main_table = [["#1 - Jerk Chicken Breast", "$8.50", "#6 - Rice & Peas", "$6.00", "#11 - Rum Punch", "$10.00"],["#2 - Rasta Pasta","$12.00", "#7 - Macaroni Pie", "$5.50", "#12 - Fruit Punch","$5.50"], ["#3 - Oxtail","$17.00", "#8 - Cabbage", "$3.50", "#13 - Peach Mango Juice","$5.50"],["#4 - Jerk Salmon","$13.00", "#9 - Mashed Potatoes", "$3.50", "#14 - Guava Pineapple","$5.50"],["#5 - Roti","$10.00", "#10 - Sweet Plantain", "$3.50", "#15 - Bottled Water","$1.50"]]
            main_headers = ["MAIN DISHES", "Price", "SIDE DISHES", "Price", "BEVERAGES", " Price"]
            print("\n",tabulate(main_table, main_headers, tablefmt="simple"))
            print("\n")

    def new_print_menu(self):
        menu_item = ["Jerk Chicken Breast", "Rasta Pasta", "Oxtail", "Jerk Salmon", "Roti", "Rice & Peas", "Macaroni Pie", "Cabbage", "Mashed Potatoes", "Sweet Plantain", "Rum Punch", "Fruit Punch", "Peach Mango Juice", "Guava Pineapple", "Bottled Water"]
        unit_price = [8.50, 12.00, 17.00, 13.00, 10.00, 6.00, 5.50, 3.50, 3.50, 3.50, 10.00, 5.50, 5.50, 5.50, 1.50]
        menu_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        menu_category = ["Main Dishes", "Side Dishes", "Beverages"]
        print("\n")
        for i in range(15):
            print(f"#{menu_number[i]} {menu_item[i]} --- ${unit_price[i]:.2f}")
        print("\n")

#discount_total = "DISCOUNT TOTAL: ${:.2f}".format(discount_total)

Menu = Menu()
#Menu.print_menu()
Menu.new_print_menu()
