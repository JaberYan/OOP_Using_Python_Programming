class Calculator:
    brand = 'Casio MS990'
    def add(self,a,b):
        return a+b
    def subs(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    
    
my_calculator=Calculator()
print(my_calculator.add(7,7))
print(my_calculator.subs(7,7))
print(my_calculator.mul(7,7))
print(my_calculator.div(7,7))