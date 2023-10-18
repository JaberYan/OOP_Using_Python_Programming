balance = 3000
def buy_thigs(item,price):
    global balance
    balance=balance-price
    dream_pnone='xphone'
    print(f'My dream phone is : {dream_pnone}')
    print(f'previous balance {item} :',balance)
    # balance=balance-price
    print(f'balnce after buying {item} :',balance)
buy_thigs('sungalss',2000)