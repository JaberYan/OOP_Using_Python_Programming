n=int(input())
a=[0,1,1]
for i in range(3,n):
    fibo=a[i-1]+a[i-2]
    a.append(fibo)
for i in range(n):
    print(a[i],end=' ')