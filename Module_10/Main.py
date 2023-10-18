from Menu import Pizza,Burger,Drinks,Menu
from Reastaurant import Reastaurant
from Users import Chef,Server,Manager,Customer,Cleaner,Supplier,Marketer
from Order import Orderr


def main():
    menu = Menu()
    # add pizza 
    pizza_1 = Pizza('naga pizza',800,'large',['tomato','carrot','onion'])
    pizza_2 = Pizza('sutki pizza',900,'medium',['sutki','oil'])
    pizza_3 = Pizza('chicken pizza',500,'small',['chicked' ,'onion'])
    menu.add_menu_item('pizza',pizza_1)
    menu.add_menu_item('pizza',pizza_2)
    menu.add_menu_item('pizza',pizza_3)
    
    # add burger
    burger_1 = Burger('naga burger',700,'beef',['naga','chili','oil'])
    burger_2 = Burger('chicken burger',900,'beef',['chicken','chili','oil'])
    menu.add_menu_item('burger',burger_1)
    menu.add_menu_item('burger',burger_2)
    
    # add drinks
    drink_1 = Drinks('lal pani',300,True)
    drink_2 = Drinks('nil pani',50,True)
    drink_3 = Drinks('kala pani',75,False)
    menu.add_menu_item('drink',drink_1)
    menu.add_menu_item('drink',drink_2)
    menu.add_menu_item('drink',drink_3)
    
    # show menu
    # menu.show_menu()
    
    
    # create reastaurent 
    restaurant = Reastaurant('sai baba restaurent',2000,menu)
    
    # add employees 
    manager = Manager('Lal mia',89,'lal@mia.com','lalpur',1600,'core','1-december-2020')
    restaurant.add_employee('manager',manager)
    
    chef = Chef('rustom baburci',90,'chupa@rustom.com','rustomNagar',3200,'chef','3-january-2021','everything')
    restaurant.add_employee('chef',chef)
    
    server = Server('chuto',78,'nai@jai.com','restaurant',300,'server','2-march-2020')
    restaurant.add_employee('server',server)
    
    # show employee
    # restaurant.show_employees()
    
    # customer 1
    customer_1 = Customer('jaber',90,'jaber@ahmed.com','sunamgonj',1200)
    
    # order 1
    order_1 = Orderr(customer_1,[pizza_3,drink_1,burger_1,drink_2])
    customer_1.pay_for_order(order_1)
    restaurant.add_orders(order_1)
    
    #paying customer for order_1
    restaurant.receive_payment(2000,order_1,customer_1)
    print('revenue and balance after first customer :',restaurant.revenue , restaurant.balance)
    
    print('\n-------------------------------------------------------')
    # customer 2
    customer_2 = Customer('riyan',89,'riyan@jabe.com','banipur',12000)
    
    #order 2
    order_2 = Orderr(customer_2,[pizza_1,burger_1,drink_1,burger_1])
    customer_2.pay_for_order(order_2)
    restaurant.add_orders(order_2)
    
    #paying customer for order_2
    restaurant.receive_payment(2000,order_2,customer_2)
    print(f'reveneu and balance after second customer :',restaurant.revenue,restaurant.balance)
    
    print('\n------------------------------------------------------------')
    # pay rent
    restaurant.pay_expence(restaurant.rent,'rent')
    print(f'reveneu and balance after paying rent :',restaurant.revenue,restaurant.balance)
    
    print(f'\n-----------------------------------------------------------')
    # paying salary 
    restaurant.add_balance_bypus(2000)
    restaurant.add_balance_bypus(2000)
    restaurant.pay_salary(chef,'chef')
    print(f'reveneu and balance after paying salary :',restaurant.revenue,restaurant.balance,restaurant.expence)
    
    print(f'\n-------------------------------------------------------------')
    restaurant.pay_expence(restaurant.rent,'rent')
    print(f'reveneu and balance after paying again rent :',restaurant.revenue,restaurant.balance,restaurant.expence)
    
    menu.remove_pizza(pizza_3)
    
    
        
if __name__ == '__main__':
    main()