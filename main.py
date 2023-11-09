class food:
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price
Burger1 = food("Beef Burger", "Burger", "Angus Beef Burger", 5.00)
Burger2 = food("Chicken Sandwhich", "Burger", "Seasoned Chicken Sandwich", 5.00)
Burger3 = food("Fish Sandwich", "Burger", "Fresh Salmon Sandwich", 7.00)
Side1 = food("Curly Fries", "Side", "Seasoned Curly Fries", 2.00)
Side2 = food("Onion Rings", "Side", "Seasoned Onion Rings", 3.00)
Side3 = food("Cheese Curds", "Side", "Seasoned Cheese CUrds", 4.00)
Drink1 = food("Coca-Cola", "Drink", "Classic Coke Taste", 1.50)
Drink2 = food("Pepsi", "Drink", "Classic Pepsi Taste", 1.50)
Drink3 = food("Root Beer", "Drink", "Classic Root Beer Taste", 1.50)
Combo1 = food("Combo 1", "Combo", "Comes With Beef Burger, Curly Fries, And Coca-Cola", 7.00)
Combo2 = food("Combo 2", "Combo", "Comes With Chicken Sandwich, Onion Rings, And Pepsi", 7.00)
Combo3 = food("Combo 3", "Combo", "Comes With Fish Sandwich, Cheese Curds, And Root Beer", 7.00)