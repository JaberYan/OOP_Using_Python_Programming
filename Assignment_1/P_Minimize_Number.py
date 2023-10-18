N=int(input())
arr=list(map(int, input().split()))
max_operetion=0
all_even =True

for num in arr:
    if num%2!=0:
        all_even =False
        break

while all_even:
    max_operetion +=1
    for i in range(N):
            arr[i] //=2
    all_even =True
    for num in arr:
        if num % 2 !=0:
            all_even =False
            break
print(max_operetion)