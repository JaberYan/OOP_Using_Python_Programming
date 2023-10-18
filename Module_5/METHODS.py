class Phone:
    price = 9000
    brand = 'walton'
    model = 'HM5'
    features = ['camera','speaker','calling','proccessor','ram','rom','charger']
    
    def call(self):
        print('calling one person')
        
    def send_sms(s,phone,sms):
        txt = f'sinding sms to : {phone} and the sms is : {sms}'
        return txt
    
my_phone = Phone()
my_phone.call()
print()
print(my_phone.features)
print()
result = my_phone.send_sms(904095,'i forgot to miss you')
print(result)