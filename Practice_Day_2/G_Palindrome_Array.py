n=int(input())
input_list=list(map(int,input().split()))
reversed_list=list(reversed(input_list))
if(input_list==reversed_list):
    print("YES")
else: 
    print("NO")