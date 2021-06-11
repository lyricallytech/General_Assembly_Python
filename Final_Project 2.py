# SHARIF TASSY: FINAL PROJECT

# Welcome to 'Rïf's Caribbean Social! 
# Your local favorite West Indian restaurant

# Class #1: Menu
    # Class #1 Methods:
        # - Print Menu

# Class #2: Place Order
    # Class #2 Methods: 
        # - Place Order
        # - List Order
        # - Print Total
        # - Apply Discount (Private Method)

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
            # side_table = [["Rice & Peas","$6.00"],["Macaroni Pie","$5.50"], ["Cabbage","$3.50"],["Mashed Potatoes","$3.50"],["Sweet Plantain","$3.50"]]
            # side_headers = ["Sides", "Price"]
            # beverages_table = [["Rum Punch","$7.00"],["Fruit Punch","$5.50"], ["Peach Mango Juice","$5.50"],["Guava Pineapple","$5.50"],["Bottled Water","$1.50"]]
            # beverages_headers = ["Beverages", "Price"]
            print("\n",tabulate(main_table, main_headers, tablefmt="simple"))
            # print("\n",tabulate(side_table, side_headers, tablefmt="simple"))
            # print("\n",tabulate(beverages_table, beverages_headers, tablefmt="simple"))
            print("\n")

class Place_Order():
    def __init__(self, *args, **kwargs):
        #self.__discount == discount
        pass

    def Place_Order(self, *args, **kwargs):
        self.order_total = float(0)
        # self.order_items = args
        for menu_item in args:
            if menu_item == 1:
                self.order_total = float(self.order_total) + float(8.50)
            elif menu_item == 2:
                self.order_total = float(self.order_total) + float(12.00)
            elif menu_item == 3:
                self.order_total = float(self.order_total) + float(17.00)
            elif menu_item == 4:
                self.order_total = float(self.order_total) + float(13.00)
            elif menu_item == 5:
                self.order_total = float(self.order_total) + float(10.00)
            elif menu_item == 6:
                self.order_total = float(self.order_total) + float(6.00)
            elif menu_item == 7 or menu_item == 12 or menu_item == 13 or menu_item == 14:
                self.order_total = float(self.order_total) + float(5.50)
            elif menu_item == 8 or menu_item == 9 or menu_item == 10:
                self.order_total = float(self.order_total) + float(3.50)
            elif menu_item == 11:
                self.order_total = float(self.order_total) + float(10.00)
            elif menu_item == 15:
                self.order_total = float(self.order_total) + float(1.50)
        #print("TOTAL: $", self.order_total)
        self.List_Order(*args)
        #self.Print_Total(*args)

    def List_Order(self, *args):
        print("\n")
        if 1 in args:
            self.jerk_chicken = 1
            jerk_chicken_count = args.count(self.jerk_chicken)
            print(f"{jerk_chicken_count}x Jerk Chicken")
        if 2 in args:
            self.rasta_pasta = 2
            rasta_pasta_count = args.count(self.rasta_pasta)
            print(f"{rasta_pasta_count}x Rasta Pasta")
        if 3 in args:
            self.oxtail = 3
            oxtail_count = args.count(self.oxtail)
            print(f"{oxtail_count}x Oxtail")
        if 4 in args:
            self.jerk_salmon = 4
            jerk_salmon_count = args.count(self.jerk_salmon)
            print(f"{jerk_salmon_count}x Jerk Salmon")
        if 5 in args:
            self.roti = 5
            roti_count = args.count(self.roti)
            print(f"{roti_count}x Roti")
        if 6 in args:
            self.rice_peas = 6
            rice_peas_count = args.count(self.rice_peas)
            print(f"{rice_peas_count}x Rice & Peas")
        if 7 in args:
            self.macaroni = 7
            macaroni_count = args.count(self.macaroni)
            print(f"{macaroni_count}x Macaroni")
        if 8 in args:
            self.cabbage = 8
            cabbage_count = args.count(self.cabbage)
            print(f"{cabbage_count}x Cabbage")
        if 9 in args:
            self.mashed_potatoes = 9
            mashed_potatoes_count = args.count(self.mashed_potatoes)
            print(f"{mashed_potatoes_count}x Mashed Potatoes")
        if 10 in args:
            self.sweet_plantain = 10
            sweet_plantain_count = args.count(self.sweet_plantain)
            print(f"{sweet_plantain_count}x Sweet Plantain")
        if 11 in args:
            self.rum_punch = 11
            rum_punch_count = args.count(self.rum_punch)
            print(f"{rum_punch_count}x Rum Punch")
        if 12 in args:
            self.fruit_punch = 12
            fruit_punch_count = args.count(self.fruit_punch)
            print(f"{fruit_punch_count}x Fruit Punch")
        if 13 in args:
            self.peach_mango_juice = 13
            peach_mango_count = args.count(self.peach_mango_juice)
            print(f"{peach_mango_count}x Peach Mango Juice")
        if 14 in args:
            self.guava_pineapple = 14
            guava_pineapple_count = args.count(self.guava_pineapple)
            print(f"{guava_pineapple_count}x Guava Pineapple")
        if 15 in args:
            self.bottled_water = 15
            bottled_water_count = args.count(self.bottled_water)
            print(f"{bottled_water_count}x Bottled Water")
        print("\n")

    def Print_Total(self): 
        total = "TOTAL: ${:.2f}".format(self.order_total)
        print(total)
        #print("\n")
        #self.order_total

    def Apply_Discount(self):
        # 20% DISCOUNT
        #print("Successful public method printed")
        self.__Apply_Discount()


    # PRIVATE METHOD
    def __Apply_Discount(self):
        # 20% DISCOUNT
        #print("Successful private method printed")
        discount_total = self.order_total * .20
        discount_total = self.order_total - discount_total
        discount_total = "DISCOUNT TOTAL: ${:.2f}".format(discount_total)
        print(discount_total)
        print("\n")


    def Credit_Card_Payment(self):
        # 4-digit number (Mock-credit card)
        credit_card = int(input("Credit Card : "))
        if type(credit_card) == int:
            time.sleep(1)
            print("\n")
            print("Pending...")
            time.sleep(1)
            print("Pending...")
            time.sleep(1)
            print("Pending...")
            #print("\n")
            time.sleep(2)
            print("Success - Charge Authorized")
            print("\n")
            print("Thank you for your support and enjoy your meal! We hope to see you soon!")
            print("\n")



Menu = Menu()
Menu.print_menu()

# 1 - Jerk Chicken Breast       # 6 - Rice & Peas               # 11 - Rum Punch                     
# 2 - Rasta Pasta               # 7 - Macaroni Pie              # 12 - Fruit Punch
# 3 - Oxtail                    # 8 - Cabbage                   # 13 - Peach Mango Juice
# 4 - Jerk Salmon               # 9 - Mashed Potatoes           # 14 - Guava Pineapple 
# 5 - Roti                      # 10 - Sweet Plantain           # 15 - Bottled Water 

ready_to_order = input("Review Order : (Y/N) ")
try:
    while ready_to_order != "Y":
        ready_to_order = input("Review Order : (Y/N) ")
    Place_Order = Place_Order()
    # ENTER ORDER NUMBERS HERE:
    Place_Order.Place_Order(1,3,4)                      # <-------------- ENTER ORDER NUMBERS HERE
    # ENTER ORDER NUMBERES ABOVE
    Place_Order.List_Order
except ValueError:
    ready_to_order = input("Review Order : (Y/N) ")

checkout_total = input("Checkout Total : (Y/N) ")
try:
    while checkout_total != "Y":
        checkout_total = input("Checkout Total : (Y/N) ")
    print("\n")
    #Place_Order = Place_Order()
    Place_Order.Print_Total()
    discount_code = input("DISCOUNT CODE : ")
    if discount_code == "GA20":
        print("\n20% Discount Applied")
        Place_Order.Apply_Discount()
        #print("\n")
        Place_Order.Credit_Card_Payment()
    elif discount_code != "GA20": 
        Place_Order.Print_Total()
        Place_Order.Credit_Card_Payment()
        #print("\n")
except ValueError:
    checkout_total = input("Checkout Total : ")





