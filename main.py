import POS_terminal as POS

burger1 = POS.Food("Beef Burger", "Burger", "Angus Beef Burger", 5.00)
burger2 = POS.Food("Chicken Sandwich", "Burger", "Seasoned Chicken Sandwich", 5.00)
burger3 = POS.Food("Fish Sandwich", "Burger", "Fresh Salmon Sandwich", 7.00)
side1 = POS.Food("Curly Fries", "Side", "Seasoned Curly Fries", 2.00)
side2 = POS.Food("Onion Rings", "Side", "Seasoned Onion Rings", 3.00)
side3 = POS.Food("Cheese Curds", "Side", "Seasoned Cheese Curds", 4.00)
drink1 = POS.Food("Coca-Cola", "Drink", "Classic Coke Taste", 1.50)
drink2 = POS.Food("Pepsi", "Drink", "Classic Pepsi Taste", 1.50)
drink3 = POS.Food("Root Beer", "Drink", "Classic Root Beer Taste", 1.50)
combo1 = POS.Food("Combo 1", "Combo", "Comes With Beef Burger, Curly Fries, And Coca-Cola", 7.00)
combo2 = POS.Food("Combo 2", "Combo", "Comes With Chicken Sandwich, Onion Rings, And Pepsi", 7.00)
combo3 = POS.Food("Combo 3", "Combo", "Comes With Fish Sandwich, Cheese Curds, And Root Beer", 7.00)

print('Hello! Welcome to The Burger Joint! Here is our menu: \n')

if __name__ == "__main__":
    POS.take_order()
