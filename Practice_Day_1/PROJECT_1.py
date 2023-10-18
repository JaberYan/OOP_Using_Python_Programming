class Product:
    
    def __init__(self,product_name) -> None:
        self.product_name = product_name
    
class Shop:
    
    def __init__(self,shop_name) -> None:
        self.shopName = shop_name
        self.products = []
        
    def add_product(self,product):
        self.products.append(product)
         
    def buy_product(self,name):
        for i in range(len(self.products)):
            if name in self.products[i].product_name:
                print("congress")
                return
        print("not available")
        
        
            
jaber_store = Shop('riyan_store')
moyda_odj = Product('moyda')
carrot_obj = Product('caroot')
jaber_store.add_product(moyda_odj)
jaber_store.add_product(carrot_obj)
# jaber_store.buy_product('moyda')
jaber_store.buy_product('caroot')