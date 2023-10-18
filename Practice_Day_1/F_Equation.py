x, y = map(int, input().split())
X=x
Y=y
summ=0
for i in range(y):
    if(i%2==0):
        summ+=x**i
print(summ-1)