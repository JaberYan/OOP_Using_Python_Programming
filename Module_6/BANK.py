class Bank:
    def __init__(self,holder_name,initial_balance) -> None:
        self.holder_name = holder_name # public
        self._brance = 'joynogor' #protected
        self.__balance = initial_balance #private
        
    def deposite(self , amount):
        self.__balance+=amount
        
    def get_balance(self):
        return f'the balance of your account : {self.__balance}'
    
jaber = Bank('jaber',8000)
jaber.deposite(8000)
print(jaber.get_balance())
print(jaber._brance)
# print(dir(jaber))
jaber.deposite(7000)
print(jaber._Bank__balance)