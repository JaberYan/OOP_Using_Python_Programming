import random

class Bank:
    total_balance_of_bank = 0
    total_loan_of_bank = 0
    
    @classmethod
    def update_total_balance(self, amount):
        self.total_balance_of_bank += amount
    
    @classmethod
    def update_total_loan(self, amount):
        self.total_loan_of_bank += amount
    
    def __init__(self):
        self.admin = Admin(self)
        
    users = []
    @classmethod
    def user_add(self,user):
        self.users.append(user)


    def create_user(self, name, email, address, account_type,password):
        user = User(name, email, address, account_type, self.admin,password)
        self.user_add(user)
        print('----------------------------------------')
        print("<<Account created Successfully>>")
        print('----------------------------------------')
        # print(self.users[0].name,self.users[0].Balance)

    def delete_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print('----------------------------------------')
            print("<<<Delete user successfully>>>")
            print('----------------------------------------')
        else:
            print('----------------------------------------')
            print("No User found")
            print('----------------------------------------')

    def get_all_users(self):
        for user in self.users:
            print('--------------------------------------------')
            print(f"Name: {user.name}, Account Number: {user.account_number}, Type: {user.account_type}")
            print('--------------------------------------------')

    def get_total_balance(self):
        # total_balance = sum(user.Balance for user in self.users)
        # total_balance = 0
        # for user in self.users:
        #     total_balance += user.Balance
        print('--------------------------------------------')
        print("Total balance is: $", self.total_balance_of_bank)
        print('--------------------------------------------')
        
        
    def get_total_loan_amount(self):
        # total_loan_amount = sum(user.loan_amount for user in self.users)
        print('--------------------------------------------')
        print("Total loan is: $", self.total_loan_of_bank)
        print('--------------------------------------------')

    def loan_feature(self):
        admin.is_loan_enabled = not admin.is_loan_enabled
        status = "enabled" if admin.is_loan_enabled else "disabled"
        print('--------------------------------------------')
        print(f"Loan feature {status}")
        print('--------------------------------------------')

        
class User:
    
    def __init__(self,name, email, address, account_type,adminn,password):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.password = password
        self.account_number = random.randint(100000, 999999)
        self.Balance = 0
        self.loan_count = 0
        self.loan_amount = 0
        self.adminn = adminn
        # self.bankk = Bank()
        self.transaction_list = []
        
    def create_user(sefl,name,email,address,account_type,password):
        Bank().create_user(name,email,address,account_type,password)
     
        
    def deposite(self,amount):
        self.Balance += amount
        Bank.update_total_balance(amount)
        self.transaction_list.append(f'Deposite : ${amount}')
        print('------------------------------------')
        print(f"<<<{amount} TK Deposit Successful and Total balance is {self.Balance}>>>")
        print('------------------------------------')


    def withdraw(self, amount):
        if amount > self.Balance:
            print('------------------------------------')
            print("Withdrawal amount exceeded. Insufficient funds.")
            print('------------------------------------')
        else:
            self.Balance -= amount
            # Bank.total_balance_of_bank(-amount)
            self.transaction_list.append(f"Withdrew: ${amount}")
            print('------------------------------------')
            print(f"<<<{amount} TK Withdrawal Successful and Total balance is {self.Balance}>>>")
            print('------------------------------------')


    def check_balance(self):
        print('------------------------------------')
        print(f'Total balance is : ${self.Balance}')
        print('------------------------------------')


    def check_transaction_history(self):
        print('------------------------------------')
        print(self.transaction_list)
        print('------------------------------------')


    def take_loan(self, amount):
        true_false = self.adminn.is_loan_enabled
        
        # if self.loan_count <= 2 or true_false is not False:
            
        if self.loan_count == 2 or true_false is False:
            print('-------------------------------------------------------------------------------')
            print("You have reached the maximum loan limit or the bank's loan feature is disabled.")
            print('-------------------------------------------------------------------------------')
        else:
            Bank.update_total_loan(amount)
            self.loan_count += 1
            # self.loan_amount += amount
            self.Balance += amount
            self.transaction_list.append(f"Loan approved: ${amount}")
            print('------------------------------------')
            print("<<<Loan Approved>>>")
            # print("Count Loan : ", self.loan_count)
            print('------------------------------------')


    def transfer(self, recipient, amount):
        if recipient in Bank().users:
            recipient.deposite(amount)
            self.withdraw(amount)
            self.transaction_list.append(f"Transferred ${amount} to {recipient.name}")
        elif amount > self.Balance:
            print('------------------------------------')
            print("Transfer failed. Insufficient funds.")
            print('------------------------------------')
        else:
            print('------------------------------------')
            print("Error: Account does not exist.")
            print('------------------------------------')
            
            

class Admin:
    def __init__(self, bank):
        self.bank = bank
        self.user = User(None,None,None,None,None,None)
        self.is_loan_enabled = True


    def create_user(self, name, email, address, account_type,password):
        self.bank.create_user(name, email, address, account_type,password)


    def delete_user(self, user):
        self.bank.delete_user(user)


    def get_all_users(self):
        self.bank.get_all_users()


    def check_total_balance(self):
        print(self.bank.get_total_balance())


    def check_total_loan_amount(self):
        self.bank.get_total_loan_amount()


    def loan_feature(self):
        self.bank.loan_feature()




'--------------MAIN FUNCTION--------------'
bank_system = Bank()
userr = User(None,None,None,None,Admin(bank_system),None)
admin = Admin(bank_system)
current_user = None
print("\nWelcome to Apna Bank\n")
print("Are you Admin/User??")
print("1. Admin")
print("2. User")
print("3. Exit")
user_type =input("Choice Option for login admin/user: ")

while True:
    
    if user_type == "1":
        print("\nADMIN ID: 'admin' AND PASS: '123'\n")
        print("Login for Admin\n")
        id = input("ENTER ID: ")
        pas = input("ENTER PASSWORD: ")
        if id == 'admin' and pas == '123':
            print("\nAdmin Successfully Logged in\n")
            print("1. Create an account\n")
            print("2. Delete an account\n")
            print("3. See all Users\n")
            print("4. Total Available Balance\n")
            print("5. Check total loan amount\n")
            print("6. Loan Off/On feature\n")
            print("7. LOGOUT TO ADMIN\n")
            select = int(input("ENTER THE OPTION: "))
            if select == 1:
                name = input("ENTER THE NAME: ")
                email = input("ENTER THE EMAIL: ")
                address = input("ENTER THE ADDRESS: ")
                account_type = input("ENTER THE ACCOUNT_TYPE: ")
                password = input("ENTER PASSWORD: ")
                admin.create_user(name, email, address, account_type,password)
                addd= User(name,email,address,account_type,None,password)
                current_user = addd.account_number
                
                
            elif select == 2:
                account_number_to_delete = int(input("ENTER ACCOUNT NUMBER TO DELETE: "))
                user_to_delete = next((user for user in bank_system.users if user.account_number == account_number_to_delete), None)
                if user_to_delete:
                    admin.delete_user(user_to_delete)
                else:
                    print("User not found.")
                    
            elif select == 3:
                admin.get_all_users()
                
            elif select == 4:
                admin.check_total_balance()
                
            elif select == 5:
                admin.check_total_loan_amount()
                
            elif select == 6:
                admin.loan_feature()
                
            elif select == 7:
                print("Admin LogOut\n")
                print("\nWelcome to Apna Bank\n")
                print("Are you Admin/User??")
                print("1. Admin")
                print("2. User")
                print("3. Exit")
                user_type =input("Choice Option for login admin/user: ")
                # break
        else:
            print("Invalid Admin, Plz enter currect admin id and pass")
            print("\nWelcome to Apna Bank\n")
            print("Are you Admin/User??")
            print("1. Admin")
            print("2. User")
            print("3. Exit")
            user_type =int(input("Choice Option for login admin/user: "))
        
        
        
        
    # Inside the while loop where user_type is 2:
    elif user_type == "2":
        if current_user == None:
            print("\nThere are no user available in bank ,Creat user from Admin, Well you should back to admin")
            print("Invalid Admin, Plz enter currect admin id and pass")
            print("\nWelcome to Apna Bank\n")
            print("Are you Admin/User??")
            print("1. Admin")
            print("2. User")
            print("3. Exit")
            user_type =input("Choice Option for login admin/user: ")
            
        else:
            print("\nLogin for User\n")
            user_name = input("Enter User Name: ")
            user_acc_no = int(input("Enter User Account Number: "))  
            print()    
            
            valid_user = None
            for u in bank_system.users:
                if u.name == user_name and u.account_number == user_acc_no:
                    valid_user = u
                    break
            
            if valid_user:
                userr = valid_user
                print("1. Withdraw\n")
                print("2. Deposit\n")
                print("3. Check Available balance\n")
                print("4. Check transaction History\n")
                print("5. Take a loan\n")
                print("6. Transfer Money\n")
                print("7. LOGOUT TO USER\n")
                select = int(input("ENTER THE OPTION: "))
                
                if select == 1:
                    amount = int(input("ENTER WITHDRAW AMOUNT: "))
                    userr.withdraw(amount)
                    
                elif select == 2:
                    amount = int(input("ENTER DEPOSIT AMOUNT : "))
                    userr.deposite(amount)
                    
                elif select == 3:
                    userr.check_balance()
                    
                elif select == 4:
                    userr.check_transaction_history()
                    
                elif select == 5:
                    amount = int(input("ENTER LOAN AMOUNT: "))
                    userr.take_loan(amount)
                    
                elif select == 6:
                    account_number = int(input("ENTER ACCOUNT NUMBER TO TRANSFER TO: "))
                    valid_recipient = next((u for u in bank_system.users if u.account_number == account_number), None)
                    if valid_recipient:
                        amount = int(input("ENTER AMOUNT TO TRANSFER: "))
                        userr.transfer(valid_recipient, amount)
                    else:
                        print('----------------------------')
                        print("Recipient account not found.")
                        print('----------------------------')
                        
                elif select == 7:
                    print("\nWelcome to Apna Bank\n")
                    print("Are you Admin/User??")
                    print("1. Admin")
                    print("2. User")
                    print("3. Exit")
                    user_type =input("Choice Option for login admin/user: ")
            else:
                print("---------------------------------------------------------------")
                print("User Not Found, Please enter valid user Name and Account number")    
                print("---------------------------------------------------------------")


    else:
        break