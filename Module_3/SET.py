#list -->[]
#tuple -->()
#set -->{}

#set -->unique value collection. no duplicate value
numbers=[1,2,3,4,5,6,6,10,9,10]
numbers_set=set(numbers)
print(numbers)
numbers_set.add(90)
print(numbers_set)
print(len(numbers))
print(len(numbers_set))
for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print("9 number exist in the set")
if 10 in numbers_set:
    print("10 number exist in the set")
else:
    print("no one exist")
A={1,3,4,5}
B={1,4,6,3}
print(A.union(B)) #sob gule niye ne
print(A.intersection(B)) #common gula niye ne
print("same as uporer gula")
print(A | B)
print(A&B)