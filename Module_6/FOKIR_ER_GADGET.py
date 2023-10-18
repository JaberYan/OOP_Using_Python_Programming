class Laptop:
    def __init__(self,name,brand,color,memory,price):
        self.name = name
        self.brand = brand
        self.color = color
        self.memory = memory
        self.price = price
        
    def run(self):
        return f'runing the laptop : {self.brand}'
    
    def coding(self):
        return f'leaning python and practicing'
    
class Phone:
    def __init__(self,brand,color,dual,price,name) -> None:
        self.brand = brand
        self.color = color
        self.dual = dual
        self.price = price
        self.name = name
        
    def phone_call(self,number,txt):
        return f'sending SMS to : {number} with : {txt}'

class Camera:
    def __init__(self,brand , price ,color ,pixel) -> None:
        self.brand = brand
        self.price = price 
        self.color = color
        self.pixel = pixel
        
    def camera_shoting(self):
        return f'camera is busy to take photo celebrity'
    
    def lence_change(self):
        pass
    
