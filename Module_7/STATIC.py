#static method @staticmethod 
#class method @classmethod
#deffrence of static method between class method 

class Shopping:
    cart = []
    origin = 'china'
    
    def __init__(self,name,location) -> None:
        self.name = 'mute elam sunargoan'
        self.location = 'narayangonj'
        
    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'buying {item} for price : {price} remaining : {remaining}')
    
    @staticmethod
    def add(a,b):
        result = a+b
        print(result)
    
    
    @staticmethod
    def sub(a,b):
        result = a-b
        print(result)
    
    
    @staticmethod
    def mutiply(a,b):
        result = a*b
        print(result)
    
    
    @staticmethod
    def div(a,b):
        result = a/b
        print(int(result))
    
       
    @classmethod
    def hudai_dekhi(self,item):
        print(f'kicu kinmu na hudai {item} dekhmu ar ac er hawa khamu')
    
# Shopping.purchase('a','lungi',400,800)
# basundara = Shopping('basundara','jani na')
# basundara.purchase('lungi',500,1000)
Shopping.hudai_dekhi('lungi') #class method

Shopping.add(8,8) #static method
Shopping.sub(8,8) #static method
Shopping.mutiply(8,8) #static method
Shopping.div(6,3) #static method