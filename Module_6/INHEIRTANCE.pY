#base class , parent class

class Gadget:
    def __init__(self,brand,color,price,origin) -> None:
        self.brand = brand
        self.color = color
        self.price = price
        self.origin = origin
        
    def run(self):
        return f'rinning the {self.brand}' 
        
class Laptop:
    def __init__(self,memory):
        self.memory = memory
    
    def coding(self):
        return f'leaning python and practicing'
    
#derived class

class Phone(Gadget):
    def __init__(self,dual,brand,color,price,origin) -> None:
        self.dual = dual
        super().__init__(brand,color,price,origin)
        
    def phone_call(self,number,txt):
        return f'sending SMS to : {number} with : {txt}'
    
    def __repr__(self) -> str:
        return f'phone : {self.brand} {self.color} {self.price} {self.origin} {self.dual}'

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel
        
    def camera_shoting(self):
        return f'camera is busy to take photo celebrity'
    
    def lence_change(self):
        pass
    
    
my_phone = Phone(True,'walton','red',9000,'bangladesh')
print(my_phone)