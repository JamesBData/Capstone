from decimal import Decimal


class Food:
    menu = []

    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = Decimal(price).quantize(Decimal("0.01"))
        Food.menu.append(self)

    def __str__(self):
        return f'{self.name}: ${self.price}'


burger1 = Food("Beef Burger", "Burger", "Angus Beef Burger", 5.00)
burger2 = Food("Chicken Sandwich", "Burger", "Seasoned Chicken Sandwich", 5.00)
burger3 = Food("Fish Sandwich", "Burger", "Fresh Salmon Sandwich", 7.00)
side1 = Food("Curly Fries", "Side", "Seasoned Curly Fries", 2.00)
side2 = Food("Onion Rings", "Side", "Seasoned Onion Rings", 3.00)
side3 = Food("Cheese Curds", "Side", "Seasoned Cheese Curds", 4.00)
drink1 = Food("Coca-Cola", "Drink", "Classic Coke Taste", 1.50)
drink2 = Food("Pepsi", "Drink", "Classic Pepsi Taste", 1.50)
drink3 = Food("Root Beer", "Drink", "Classic Root Beer Taste", 1.50)
combo1 = Food("Combo 1", "Combo", "Comes With Beef Burger, Curly Fries, And Coca-Cola", 7.00)
combo2 = Food("Combo 2", "Combo", "Comes With Chicken Sandwich, Onion Rings, And Pepsi", 7.00)
combo3 = Food("Combo 3", "Combo", "Comes With Fish Sandwich, Cheese Curds, And Root Beer", 7.00)

subtotal = []

cart = []


def show_menu(menu):
    print('===Menu===')
    for i, item in enumerate(menu, 1):
        print(f"{i}. {item}")
    print("0. Exit Menu")


def new_order():
    new_order = input("\nWould you like to start a new order? (y/n)\n> ")
    if new_order == 'y':
        cart.clear()
        subtotal.clear()
        take_order()

    elif new_order == 'n':
        print('Goodbye! Thank you for visiting The Burger Joint!')
    return


def order_again():
    order_again = input("Would you like to add to your order? (y/n)\n> ")
    if order_again == 'y':
        take_order()
    elif order_again == 'n':
        sub_total = sum(subtotal)
        sales_tax_rate = Decimal(0.06)
        sales_tax = sales_tax_rate * sub_total
        grand_total = sub_total + sales_tax
        print(f"Subtotal: ${sub_total:.2f} \n6% Sales Tax: ${sales_tax:.2f} \nGrand Total: ${grand_total:.2f}")

        print("\n==== Payment ====")
        print("1. Cash\n2. Credit Card\n3. Check")
        payment_choice = input("Select a payment type: ")

        if payment_choice == '1':
            amount_tendered = Decimal(input("Enter amount tendered: "))
            change = amount_tendered - grand_total
            print("\n==== Receipt ====")
            for item in cart:
                print(f"({item['quantity']}) {item['choice']}(s)")
            print(f'Subtotal: ${sub_total:.2f} \nGrand total: ${grand_total:.2f} \nAmount tendered: ${amount_tendered:.2f} \nChange: ${change:.2f}')
            new_order()

        elif payment_choice == '2':
            credit_card_number = int(input('Enter your 12 digit credit number: '))
            cvv = int(input('Enter your 3 digit CVV: '))
            expiration_date = int(input('Enter expiration date (Please provide just 4 digits.): '))
            print("\n==== Receipt ====")
            for item in cart:
                print(f"({item['quantity']}) {item['choice']}(s)")
            print(f'Subtotal: ${sub_total:.2f} \nGrand total: ${grand_total:.2f} \nCard processed: {credit_card_number}')
            new_order()

        elif payment_choice == '3':
            check_number = int(input('Enter your check number: '))
            print("\n==== Receipt ====")
            for item in cart:
                print(f"({item['quantity']}) {item['choice']}(s)")
            print(f'Subtotal: ${sub_total:.2f} \nGrand total: ${grand_total:.2f} \nPaid with check number: {check_number}')
            new_order()


def take_order():

    show_menu(Food.menu)
    choice = int(input("Select an item (number or '0' to finish): "))

    if choice == 0:
        print('Goodbye! Thank you for visiting The Burger Joint!')
        # break

    elif 1 <= choice <= len(Food.menu):
        item = {}
        item["choice"] = Food.menu[choice - 1].name
        item["quantity"] = int(input('Enter quantity: '))
        line_total = Food.menu[choice - 1].price * item["quantity"]
        subtotal.append(int(line_total))
        cart.append(item)

        print(f'{item["quantity"]} {Food.menu[choice - 1].name}(s) costs ${line_total}.')
        order_again()

    else:
        print("I am sorry. That entry is invalid, please try again.")


if __name__ == "__main__":
    print("Please do not run this file directly. It should be imported from a separate main.py file.")

