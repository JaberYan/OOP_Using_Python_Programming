#csv-->comma saparated value
#txt-->text file

# with open('massage.txt','w') as file:
#     file.write('Hello World!')

# with open('massage.txt','a') as file:
#     file.write('Hello World! \n')

# with open('massage.txt','r') as file:
#     txt = file.read()
#     print(txt)


txt =[['a','b'],['c','d']]
for i in txt:
    for value in i:
        print(i,':',value)
