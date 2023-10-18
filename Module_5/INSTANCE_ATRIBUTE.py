class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] #cart is an instance attribute
        
    def add_to_cart(self,item):
        self.cart.append(item)
        
jaber = Shop('Jaber')
jaber.add_to_cart('phone')
jaber.add_to_cart('pineapple')
jaber.add_to_cart('carrot')
jaber.add_to_cart('earphone')
print(jaber.buyer,':',jaber.cart)
print()
mahnaz = Shop('Mahnaz')
mahnaz.add_to_cart('leepstick')
mahnaz.add_to_cart('iliner')
mahnaz.add_to_cart('phone')
mahnaz.add_to_cart('earphone')
print(mahnaz.buyer,':',mahnaz.cart)