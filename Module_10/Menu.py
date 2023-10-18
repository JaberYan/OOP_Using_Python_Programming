class Food:
    def __init__(self ,name , price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 10

class Pizza(Food):
    def __init__(self, name, price , size , toppings=[]) -> None:
        self.size = size
        self.ingredients = toppings
        super().__init__(name, price)
        
class Burger(Food):
    def __init__(self, name, price ,meat , ingredients) -> None:
        self.meat = meat
        self.ingredients = ingredients
        super().__init__(name, price)
        
class Drinks(Food):
    def __init__(self, name, price ,isCold = True) -> None:
        super().__init__(name, price)
        self.isCold = isCold

class Juice(Food):
    def __init__(self, name, price) -> None:
        super().__init__(name, price)
    pass

class Salad(Food):
    def __init__(self, name, price) -> None:
        super().__init__(name, price)
    pass

class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []
        
    def add_menu_item(self,item_type,item):
        if item_type == 'pizza':
            self.pizzas.append(item)
            
        elif item_type == 'burger':
            self.burgers.append(item)
        
        elif item_type == 'drink':
            self.drinks.append(item)
            
    def remove_pizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
        print('------------------Pizza-------------------------')
        for pizza in self.pizzas:
            print(f'name : {pizza.name} ,and price : {pizza.price} ,size is : {pizza.size}')
        print('------------------Pizza-------------------------')
    
    def remove_burger(self,burger):
        if burger in self.burgers:
            self.burgers.remove(burger)
        print('-----------------Burger-------------------------')
        for burger in self.burgers:
            print(f'name : {burger.name} ,and price : {burger.price} ,used meat is : {burger.meat}')
        print('-----------------Burger-------------------------')
            
    def remove_drinks(self,drink):
        if drink in self.drinks:
            self.drinks.remove(drink)
        print('-----------------Drinks-------------------------')
        for drink in self.drinks:
            print(f'name : {drink.name} , and price : {drink.price} , status(cold) : {drink.isCold}')
        print('-----------------Drinks-------------------------')
            
    def show_menu(self):
        print('------------------Pizza-------------------------')
        for pizza in self.pizzas:
            print(f'name : {pizza.name} ,and price : {pizza.price} ,size is : {pizza.size}')
        print('------------------Pizza-------------------------')
        print('\n')
        print('-----------------Burger-------------------------')
        for burger in self.burgers:
            print(f'name : {burger.name} ,and price : {burger.price} ,used meat is : {burger.meat}')
        print('-----------------Burger-------------------------')
        print('\n')
        print('-----------------Drinks-------------------------')
        for drink in self.drinks:
            print(f'name : {drink.name} , and price : {drink.price} , status(cold) : {drink.isCold}')
        print('-----------------Drinks-------------------------')