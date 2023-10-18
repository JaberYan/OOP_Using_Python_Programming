#           0 1 2 3 4 5 6
numbers = [1,2,3,4,5]
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2:5])
# print(numbers[2:])
# print(numbers[:6])
# print(numbers[1:5:1])
# print(numbers[1:5:2])
# print(numbers[6:1:-1])
# print(numbers[6:1:-2])
# print(numbers[:])
# print(numbers[::-1])   #shortcut to reverse a list 
# print(numbers[::-2])
numbers.append(6)
numbers.append(7)
numbers.append(8)
for i in (9,11):
    numbers.append(i)
print(numbers)