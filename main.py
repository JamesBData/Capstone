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

class Menu:
    def __init__(self):
        self.items = [
            Food("Beef Burger", "Burger", "Angus Beef Burger", 5.00),
            Food("Chicken Sandwich", "Burger", "Seasoned Chicken Sandwich", 5.00),
            Food("Fish Sandwich", "Burger", "Fresh Salmon Sandwich", 7.00),
            Food("Curly Fries", "Side", "Seasoned Curly Fries", 2.00),
            Food("Onion Rings", "Side", "Seasoned Onion Rings", 3.00),
            Food("Cheese Curds", "Side", "Seasoned Cheese CUrds", 4.00),
            Food("Coca-Cola", "Drink", "Classic Coke Taste", 1.50),
            Food("Pepsi", "Drink", "Classic Pepsi Taste", 1.50),
            Food("Root Beer", "Drink", "Classic Root Beer Taste", 1.50),
            Food("Combo 1", "Combo", "Comes With Beef Burger, Curly Fries, And Coca-Cola", 7.00),
            Food("Combo 2", "Combo", "Comes With Chicken Sandwich, Onion Rings, And Pepsi", 7.00),
            Food("Combo 3", "Combo", "Comes With Fish Sandwich, Cheese Curds, And Root Beer", 7.00),
        ]
        self.cart = []

    def show_menu(self):
        print("==== Menu ====")
        for i, food in enumerate(self.food, 1):
            print(f"{i}. {food.name} ({food.price:.2f} USD)")
        print("M. Main Menu")

    def take_order(self):
        while True:
            self.show_menu()
            choice = int(input(f"Select an item (number or 'M' to finish): ")).strip()
            if choice.lower() == 'm':
                break
            try:
                choice, quantity = int(choice), int(input("Enter quantity: "))
                if 1 <= choice <= len(self.food) and 1 <= quantity:
                    self.cart.append((self.food[choice - 1], quantity))
                    #runtotal = sum(product.price * quantity for product, quantity in self.cart)
                    print(f"{quantity} {self.food[choice - 1].name}(s) added to the cart.")
                else:
                    print("Invalid input.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number or 'M' for the main menu.")

    def calculate_totals(self):
        subtotal = sum(food.price * quantity for food, quantity in self.cart)
        sales_tax_rate = Decimal(0.06)
        sales_tax = subtotal * sales_tax_rate
        grand_total = subtotal + sales_tax
        return subtotal, sales_tax, grand_total



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


def show_menu(menu):
    print('===Menu===')
    for i, item in enumerate(menu, 1):
        print(f"{i}. {item}")
    print("0. Main Menu")
def calculate_totals(subtotal):
    sub_total = sum(subtotal)
    tax_rate = Decimal(0.06)
    sales_tax = subtotal * tax_rate
    grand_total = sub_total + sales_tax
    return f"Your subtotal is {sub_total}, your tax is {sales_tax}, and your grand total is {grand_total}."

# show_menu(Food.menu)


# def take_order(menu):
#     cart = []
request_again_flag = True
while request_again_flag:

    show_menu(Food.menu)
    choice = int(input("Select an item (number or '0' to finish): "))
    if choice == '0':
        request_again_flag = False
    elif 1 <= choice <= len(Food.menu):
        quantity = int(input('Enter quantity: '))
        line_total = Food.menu[choice - 1].price * quantity
        subtotal.append(int(line_total))
        print(f'{quantity} {Food.menu[choice - 1].name}(s) costs ${line_total}.')

    else:
        print("Invalid input. Please enter a number or '0' for the main menu.")




    while True:
        order_again = input("Would you like to add to your order? (y/n)\n> ")
        if order_again == 'y':
                break
        elif order_again == 'n':
            calculate_totals(subtotal)
            request_again_flag = False
            break
        else:
            print("That entry is invalid, please try again.")


