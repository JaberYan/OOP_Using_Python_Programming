class Phone:
    
    #constructor
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price
        # Owner = owner
        # Brand = brand
        # Price = price
        
        
my_phone = Phone('jaber','walton',9000)
print(f'the owner of this phone {my_phone.owner} and phone brand is {my_phone.brand} and lastly price of this phone {my_phone.price}')