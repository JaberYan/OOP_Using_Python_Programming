class Vehicle:
    def __init__(self,name,price,color) -> None:
        self.name = name
        self.price = price
        self.color = color
        
    def run(self):
        pass
    
    def __repr__(self) -> str:
        return f'the vehicle name is {self.name} , price is : {self.price} , color is : {self.color}'
    
class Bus(Vehicle):
    def __init__(self, name, price, color,seat) -> None:
        self.seat = seat
        super().__init__(name, price, color)
        
    def __repr__(self) -> str:
        return super().__repr__()
        
class Truck(Vehicle):
    def __init__(self, name, price, color,weight) -> None:
        self.weight = weight
        super().__init__(name, price, color)
        
    def __repr__(self) -> str:
        return super().__repr__()
        
class PickUpTruck(Truck):
    def __init__(self, name, price, color, weight) -> None:
        super().__init__(name, price, color, weight)
        
    def __repr__(self) -> str:
        return super().__repr__()
        
class AC_Bus(Bus):
    def __init__(self, name, price, color, seat,temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, color, seat)
        
    def __repr__(self) -> str:
        return super().__repr__()
        
khailla_bus = AC_Bus('Ana',5000000,'black',22,15)
print(khailla_bus)
