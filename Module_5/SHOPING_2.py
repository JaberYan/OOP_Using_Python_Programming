class Shoping:
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []
    
    def add_to_cart(self,item,price,quantity):
        product = {'item' : item, 'price' : price , 'quantity' : quantity}
        self.cart.append(product)
        
    def checkout(self,amount):
        total = 0
        for item in self.cart:
            total+=item['price'] * item['quantity']
        if amount < total :
            print(f'Please provide {total-amount} tk more')
        else:
            print(f'your total product price {total} tk and your extra money is {amount-total} tk')
            
    
jaber = Shoping('Jaber')
jaber.add_to_cart('alu',50,6)
jaber.add_to_cart('rice',120,3)
jaber.add_to_cart('tomato',90,2)
# print(jaber.cart)
jaber.checkout(1000)

