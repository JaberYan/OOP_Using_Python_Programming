#read only --> value set kora jabe na
#getter --> value access kora jay method er help niya ar private property o access kora jay @property
#setter --> private property er value set kora jay method er help niya @method name.setter



class User:
    def __init__(self,name,age , money) -> None:
        self.name = name
        self._age = age
        self.__money = money
        
    #getter
    @property
    def boyos(self):
        print(self._age)
        
    #getter
    @property 
    def salary(self):
        print(self.__money)
    
    @salary.setter
    def salary(self,value):
        if value < 0:
            print('salary can not be negetive')
            return
        self.__money+=value
        
        
samsu = User('kupa',21,4000)
samsu.boyos
samsu.salary = 6000
samsu.salary
samsu.salary = -100
samsu.salary