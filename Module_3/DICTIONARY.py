numbers = [12,34,5,6,78,99,45]
person1 ={'Name ':'khala chan','Age':'45','Profession':'student','Address':'khalar ghat'}
print(person1['Name '])
print(person1['Profession'])
print(person1.keys())
print(person1.values)
print(person1)
#special dictionary looping
for key,value in person1.items():
    print(key,':',value)