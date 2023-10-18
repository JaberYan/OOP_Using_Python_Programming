from abc import ABC, abstractmethod

class user(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name = name
        self.phone =  phone
        self.email = email
        self.address = address
        super().__init__()
  
        
class Customer(user):
    def __init__(self, name, phone, email, address,money) -> None:
        self.wallet = money
        self.__order = None
        self.deu_amount = 0
        super().__init__(name, phone, email, address)
     
    @property   
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order=order
        
    def place_order(self,order):
        self.order = order
        self.deu_amount += order.bill
        print(f'{self.name} placed an order bill {order.bill}')
        
    def eat(self,order):
        print(f'{self.name} eating food {order.itmes}')
        
    def pay_for_order(self,amount):
        #TODO: submit to the reastaurant menager
        pass
    
    def pay_tips(self,amount_for_tips):
        pass
    
    def write_review(self,stars):
        pass
 
    
class Employee(user):
    def __init__(self, name, phone, email, address,salary,depertment,starting_date) -> None:
        self.salary = salary
        self.depertment = depertment
        self.deu = salary
        self.satrting_date = starting_date
        super().__init__(name, phone, email, address)
        
    def receive_salary(self):
        self.deu = 0
     
        
class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, depertment, starting_date,cooking_item) -> None:
        self.cooking_item = cooking_item
        super().__init__(name, phone, email, address, salary, depertment, starting_date)


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, depertment, starting_date) -> None:
        self.tips_earning = 0
        super().__init__(name, phone, email, address, salary, depertment, starting_date)
    
    def take_order(self,order):
        pass
    
    def transfer_order_to_chef(self,order):
        pass
    
    def serve_food_to_customer(self,order):
        pass
    
    def receive_tips(self,amount):
        self.tips_earning +=amount


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, depertment, starting_date) -> None:
        super().__init__(name, phone, email, address, salary, depertment, starting_date)


class Cleaner(Employee):
    def __init__(self, name, phone, email, address, salary, depertment, starting_date) -> None:
        super().__init__(name, phone, email, address, salary, depertment, starting_date)


class Supplier(Employee):
    def __init__(self, name, phone, email, address, salary, depertment, starting_date) -> None:
        super().__init__(name, phone, email, address, salary, depertment, starting_date)
    pass


class Marketer(Employee):
    def __init__(self, name, phone, email, address, salary, depertment, starting_date) -> None:
        super().__init__(name, phone, email, address, salary, depertment, starting_date)
    pass