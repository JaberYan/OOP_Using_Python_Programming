class Reastaurant:
    def __init__(self,name, rent, menu = []) -> None:
        self.name = name
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expence = 0
        self.balance = 0
        self.profit = 0
    
    def add_balance_bypus(self,amount):
        self.balance += amount
    
    def add_employee(self,employee_type,employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee
            
    def receive_payment(self,amount,order,customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            self.customer_deu = 0
            print('extra :',amount - order.bill)
        else:
            print(f'You Have No enough Money to buy all items. Pay more {abs(amount-order.bill)}')
        
    def add_orders(self,order):
        self.orders.append(order)
        
    def pay_expence(self,amount,description):
        if amount < self.balance:
            self.expence += amount
            self.balance -= amount
            print(f'Expence {amount} for {description}')
        else:
            print(f'Not enough money to pay {amount}')
            
    def pay_salary(self,employee,description):
        print(f'Paying salary for {employee.name} with salary {employee.salary}')
        if employee.salary <= self.balance:
            self.balance -= employee.salary
            self.expence += employee.salary
            employee.receive_salary()
        else:
            print(f'Not enough money to paying salary to give {description}')
            
    def show_employees(self):
        print('\n-------------------SHOWING EMPLOYEES------------------------')
        if self.manager is not None:
            print('--------------------------SHOW MANAGER---------------------------')
            print(f'manager name {self.manager.name} with salary {self.manager.salary}')
            print('-----------------------------------------------------------------')
        
        if self.chef is not None:
            print('---------------------------SHOW CHEF-------------------------------')
            print(f'chef name {self.chef.name} with salary {self.chef.salary}')
            print('-------------------------------------------------------------------')
            
        if self.server is not None:
            print('--------------------------SHOW SERVER------------------------------')
            print(f'server name {self.server.name} with salary {self.server.salary}')
            print('-----------------------------------------------------------------')