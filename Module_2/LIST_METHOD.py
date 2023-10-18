numbers=[1,2,3,4]
numbers.append(5)
print(numbers)
numbers.insert(5,6)
print(numbers)
if 5 in numbers:
    numbers.remove(5)
print(numbers)
last=numbers.pop()
print(last,numbers)
numbers.append(90)
print(numbers)
if  3 in numbers:
    index=numbers.index(3)
    print(index)
print(numbers.count(3))