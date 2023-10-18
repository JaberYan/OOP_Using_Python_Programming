class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print("vat mangso ruti kurma")
        
    def exercise(self):
        raise NotImplementedError
        
class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight) 
    
    def eat(self):
        print("vegetable")
    
    def exercise(self):
        print("gym e giye poysa diya hudai gam joray")
        
    def __add__(self,other):
        return self.name + other.name
    
    def __mul__(self,other):
        return self.height * other.height
    
    def __sub__(self,other):
        return self.age - other.age
    
    def __len__(self):
        return self.age
    
    def __eq__(self,other):
        return self.age == other.age
        
shakib = Cricketer('shakib',35,5,65,'BD')
mushi = Cricketer('mushi',36,6,70,'BD')
shakib.eat()
shakib.exercise()
print(shakib+mushi)
print(shakib * mushi)
print(mushi - shakib)
print(len(shakib))
print(shakib == mushi)