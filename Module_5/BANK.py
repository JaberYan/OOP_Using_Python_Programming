class Bank:
    
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
        
    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        if amount > 0:
            self.balance+=amount
            
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'you can not withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'you can not withdraw more than {self.max_withdraw}')
        else:
            self.balance-=amount


brac = Bank(10000)
brac.withdraw(99)
brac.withdraw(10000000)
brac.deposite(90000)
brac.withdraw(40000)
print(brac.balance)