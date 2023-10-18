class Shop:
    cart = []
    def __init__(self,buyer):
        self.buyer = buyer
        
    def add_to_cart(self,item):
        self.cart.append(item)
        
jaber = Shop('Jaber')
jaber.add_to_cart('phone')
jaber.add_to_cart('pineapple')
jaber.add_to_cart('carrot')
jaber.add_to_cart('erephone')
print(jaber.cart)