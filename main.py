from decimal import Decimal, ROUND_HALF_UP
class Food:
    menu = []

    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.items = [
            Food("Beef Burger", "Burger", "Angus Beef Burger", 5.00),
            Food("Chicken Sandwhich", "Burger", "Seasoned Chicken Sandwich", 5.00),
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
for item in Food.menu:
    print({menu})

