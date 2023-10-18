from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod # enforce all derived class to have a eat method 
    def eat(self):
        print("i need food")
    
    @abstractmethod
    def move(self):
        pass
    
class Monckey(Animal):
    def __init__(self,name) -> None:
        self.name = name
        super().__init__()
        
    def eat(self):
        print("hey nanana !, i am eating banana")
        
    def move(self):
        print("hey i am monkey")

lyka = Monckey('lyka')
lyka.eat()
lyka.move()