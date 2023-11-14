from decimal import Decimal, ROUND_HALF_UP


class Food:
    menu = []

    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = Decimal(price).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        Food.menu.append(self)

    def __str__(self):
        return f'{self.name}: ${self.price}'


burger1 = Food("Beef Burger", "Burger", "Angus Beef Burger", 5.00)
burger2 = Food("Chicken Sandwich", "Burger", "Seasoned Chicken Sandwich", 5.00)
burger3 = Food("Fish Sandwich", "Burger", "Fresh Salmon Sandwich", 7.00)
side1 = Food("Curly Fries", "Side", "Seasoned Curly Fries", 2.00)
side2 = Food("Onion Rings", "Side", "Seasoned Onion Rings", 3.00)
side3 = Food("Cheese Curds", "Side", "Seasoned Cheese CUrds", 4.00)
drink1 = Food("Coca-Cola", "Drink", "Classic Coke Taste", 1.50)
drink2 = Food("Pepsi", "Drink", "Classic Pepsi Taste", 1.50)
drink3 = Food("Root Beer", "Drink", "Classic Root Beer Taste", 1.50)
combo1 = Food("Combo 1", "Combo", "Comes With Beef Burger, Curly Fries, And Coca-Cola", 7.00)
combo2 = Food("Combo 2", "Combo", "Comes With Chicken Sandwich, Onion Rings, And Pepsi", 7.00)
combo3 = Food("Combo 3", "Combo", "Comes With Fish Sandwich, Cheese Curds, And Root Beer", 7.00)

subtotal = []

cart = []
item = {}

print("Hello! Welcome to The Burger Joint!")


def show_menu(menu):
    print('===Menu===')
    for i, item in enumerate(menu, 1):
        print(f"{i}. {item}")
    print("0. Exit Menu")


# def calculate_totals(subtotal):
#     sub_total = sum(subtotal)
#     sales_tax = 0.06 * sub_total
#     grand_total = sub_total + sales_tax
#     return f"Subtotal: ${sub_total:.2f} \n6% Sales Tax: ${sales_tax:.2f} \nGrand Total: ${grand_total:.2f}"


request_again_flag = True
while request_again_flag:

    show_menu(Food.menu)
    choice = int(input("Select an item (number or '0' to finish): "))

    if choice == '0':
        request_again_flag = False
    elif 1 <= choice <= len(Food.menu):
        item["choice"] = Food.menu[choice - 1]
        item["quantity"] = int(input('Enter quantity: '))
        line_total = Food.menu[choice - 1].price * item["quantity"]
        subtotal.append(int(line_total))
        cart.append(item)

        print(f'{item["quantity"]} {Food.menu[choice - 1].name}(s) costs ${line_total}.')

    else:
        print("I am sorry. That entry is invalid, please try again.")

    while True:
        order_again = input("Would you like to add to your order? (y/n)\n> ")
        if order_again == 'y':
            break
        elif order_again == 'n':
            sub_total = sum(subtotal)
            sales_tax = 0.06 * sub_total
            grand_total = sub_total + sales_tax
            print(f"Subtotal: ${sub_total:.2f} \n6% Sales Tax: ${sales_tax:.2f} \nGrand Total: ${grand_total:.2f}")

            print("\n==== Payment ====")
            print("1. Cash\n2. Credit Card\n3. Check")
            payment_choice: input("Select a payment type: ")

            if payment_choice == '1':
                amount_tendered = Decimal(input("Enter amount tendered: "))
                change = amount_tendered - grand_total
                print("\n==== Receipt ====")
                print(cart)

            request_again_flag = False
            break
        else:
            print("I am sorry. That entry is invalid, please try again.")


