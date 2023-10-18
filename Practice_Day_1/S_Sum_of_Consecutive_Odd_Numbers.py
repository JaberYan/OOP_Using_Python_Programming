# def sum_of_odd_numbers_between_x_and_y(x, y):
#     total_sum = 0
#     for num in range(x + 1, y):
#         if num % 2 == 1:
#             total_sum += num
#     return total_sum
# t=int(input())
# for _ in range(t):
#     x,y=map(int,input().split)
#     result=sum_of_odd_numbers_between_x_and_y(x,y)
#     print(result)
# Function to calculate the sum of odd numbers between X and Y (exclusive)
def sum_x_y(x, y):
    if(x>y):
        x,y=y,x
    total_sum = 0
    for num in range(x +1, y):
        if num % 2 == 1:
            total_sum += num
    return total_sum

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    X=x
    Y=y
    result = sum_x_y(X,Y)
    print(result)
