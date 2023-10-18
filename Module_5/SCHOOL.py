# class Student:
#     def __init__(self,name,current_class,id):
#         self.name= name
#         self.current_class = current_class
#         self.id = id
        
#     def __repr__(self):
#         return f'Student with name : {self.name}, class : {self.current_class}, then student id : {self.id}'
        
# class Teacher:
#     def __init__(self,name,subject,id) -> None:
#         self.name = name
#         self.subject = subject
#         self.id = id
        
#     def __repr__(self) -> str:
#         return f'Teacher with name : {self.name} ,subject : {self.subject} techer id : {self.id}'

# alia = Student('Alia torkari',9,2341)
# ranbeer = Teacher('douran beer','math',122343)
# print(alia)
# print()
# print(ranbeer)
class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'Sending SMS to: {phone+5}'
        return text


my_phone = Phone()
result = my_phone.send_sms(41524, 'Missy, I missed to miss you')
print(result)