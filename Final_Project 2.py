# SHARIF TASSY: FINAL PROJECT

# Welcome to 'Rïf's Caribbean Social! 
# Your local favorite West Indian restaurant

from typing import Counter, final
from tabulate import tabulate
import time

# Global Menu Item List
menu_dictionary = {
    1: {"name": "Jerk Chicken", "price": 8.50, "category": "Main Dish"},
    2: {"name": "Rasta Pasta" , "price": 12.00, "category": "Main Dish"},
    3: {"name": "Oxtail" , "price": 17.00, "category": "Main Dish"},
    4: {"name": "Jerk Salmon" , "price": 13.00, "category": "Main Dish"},
    5: {"name": "Roti" , "price": 10.00, "category": "Main Dish"},
    6: {"name": "Rice & Peas" , "price": 6.00, "category": "Side Dish"},
    7: {"name": "Macaroni Pie" , "price": 5.50, "category": "Side Dish"},
    8: {"name": "Cabbage" , "price": 3.50, "category": "Side Dish"},
    9: {"name": "Mashed Potatos" , "price": 3.50, "category": "Side Dish"},
    10: {"name": "Sweet Plantain" , "price": 3.50, "category": "Side Dish"},
    11: {"name": "Rum Punch" , "price": 10.00, "category": "Beverages"},
    12: {"name": "Fruit Punch" , "price": 5.50, "category": "Beverages"},
    13: {"name": "Peach Mango Juice" , "price": 5.50, "category": "Beverages"},
    14: {"name": "Guava Pineapple" , "price": 5.50, "category": "Beverages"},
    15: {"name": "Bottled Water" , "price": 1.50, "category": "Beverages"}
}

# CLASS MENU
class Menu:
    def __init__(self):
        pass

    # ORIGINAL: Menu in Tabulate chart format
    def print_menu(self):
            print("\n")
            print("                        Welcome to 'Rïf's Caribbean Social! ")
            print("                        ===================================")
            print("\n")
            # Formatted_Table is an empty to list that will be appended to use in the Tabulate print.
            formatted_table = []          
            for item in menu_dictionary:
                if menu_dictionary[item]['category'] == "Main Dish":
                    # New_Row is after every iteration in the for-loop to add every row piece to the empty list.
                    # >6 in the format brackets is to justify the alignment of the prices. 
                    new_row = []
                    new_row.append(f"#{item} - {menu_dictionary[item]['name']}")
                    new_row.append("${:>6.2f}".format(menu_dictionary[item]['price']))
                    new_row.append(f"#{item + 5} - {menu_dictionary[item + 5]['name']}")
                    new_row.append("${:>6.2f}".format(menu_dictionary[item + 5]['price']))
                    new_row.append(f"#{item + 10} - {menu_dictionary[item + 10]['name']}")
                    new_row.append("${:>6.2f}".format(menu_dictionary[item + 10]['price']))
                    formatted_table.append(new_row)
            headers = ["MAIN DISHES", "PRICE", "SIDE DISHES", "PRICE", "BEVERAGES", " PRICE"]
            print("\n",tabulate(formatted_table, headers, tablefmt="simple"))
            print("\n")


class Place_Order():
    def Order_Intake():
        # Take the numbers and use the append method to add to a list
        order_list = []
        Is_Order_Finished = False
        # Calculate from the dictionary the total costs from the corresponding key values         
        while Is_Order_Finished == False:
            Order_Number_As_Char = input("Enter Order #'s: ")
            try:
                Order_Number_As_Integer = int(Order_Number_As_Char)
            except:
                pass

            if Order_Number_As_Char != "D":
                if Order_Number_As_Integer in menu_dictionary:
                    print(f"{Order_Number_As_Integer} {menu_dictionary[Order_Number_As_Integer]['name']}")
                    order_list.append(Order_Number_As_Integer)
                else:
                    print("Not a menu item. Please enter again.")
            else:
                Is_Order_Finished = True
        return order_list
        

    def List_Order(order_list):
        print("\n")
        sorted_list = sorted(order_list)
        # Initial FOR loop for collating/de-duping 
        collated_list = {}
        for item in sorted_list:
            # IGNORE: This IF/ELSE is to calculate the quantity of the first for loop 
            if item in collated_list:
                collated_list[item] = collated_list[item] + 1
            else:
                collated_list[item] = 1
        # Second FOR loop for displaying the order of the items
        print("\n")
        sum = 0
        print("Ordered Items: ")
        for item in collated_list:
            order_quantity = collated_list[item]
            unit_price = menu_dictionary[item]['price']
            unit_price_formatted = "{:.2f}".format(menu_dictionary[item]['price'])
            row_total = order_quantity * unit_price
            grand_total_string = "{:.2f}".format(row_total)
            grand_total = grand_total_string
            print(f"{collated_list[item]}x - {menu_dictionary[item]['name']} - Unit Price: ${unit_price_formatted} - TOTAL: ${grand_total}")
            sum = sum + float(grand_total)
            total_sum = "{:.2f}".format(sum)
        print("\n")
        print("GRAND TOTAL: $", total_sum)
        print("\n")


    def Print_Total(self): 
        total = "TOTAL: ${:.2f}".format(self.order_total)
        print(total)

    def Apply_Discount(self):
        # 20% DISCOUNT
        self.__Apply_Discount()


    # PRIVATE METHOD
    def __Apply_Discount(self):
        # 20% DISCOUNT
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
            time.sleep(2)
            print("Success - Charge Authorized")
            print("\n")
            print("Thank you for your support and enjoy your meal! We hope to see you soon!")
            print("\n")



Menu = Menu()
Menu.print_menu()

Place_Order()

Updated_Order_Intake = Place_Order.Order_Intake()


#print("\n")
ready_to_order = input("Review Order : (Y/N) ")
while ready_to_order != "Y":
    ready_to_order = input("Review Order : (Y/N) ")

#print(Updated_Order_Intake)
Place_Order.List_Order(Updated_Order_Intake)


checkout_total = input("Checkout Total : (Y/N) ")
try:
    while checkout_total != "Y":
        checkout_total = input("Checkout Total : (Y/N) ")
    #Place_Order = Place_Order()
    #Place_Order.Print_Total()
    discount_code = input("DISCOUNT CODE : ")
    if discount_code == "GA20":
        print("\n20% Discount Applied")
        Place_Order.Apply_Discount()
        Place_Order.Credit_Card_Payment()
    elif discount_code != "GA20": 
        Place_Order.Print_Total()
        Place_Order.Credit_Card_Payment()
except ValueError:
    checkout_total = input("Checkout Total : ")





